#    Copyright 2018 Alexey Stepanov aka penguinolog.

#    Copyright 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Python subprocess.Popen wrapper."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import collections
# noinspection PyCompatibility
import concurrent.futures
import errno
import logging
import os
import subprocess  # nosec  # Expected usage
import threading
import typing  # noqa  # pylint: disable=unused-import

import six
import threaded

from exec_helpers import api
from exec_helpers import exec_result
from exec_helpers import exceptions
from exec_helpers import _log_templates

logger = logging.getLogger(__name__)  # type: logging.Logger
# noinspection PyUnresolvedReferences
devnull = open(os.devnull)  # subprocess.DEVNULL is py3.3+


class SingletonMeta(type):
    """Metaclass for Singleton.

    Main goals: not need to implement __new__ in singleton classes
    """

    _instances = {}  # type: typing.Dict[typing.Type, typing.Any]
    _lock = threading.RLock()  # type: threading.RLock

    def __call__(cls, *args, **kwargs):
        """Singleton."""
        with cls._lock:
            if cls not in cls._instances:
                # noinspection PySuperArguments
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def __prepare__(
        mcs,
        name,  # type: str
        bases,  # type: typing.Iterable[typing.Type]
        **kwargs
    ):  # type: (...) -> collections.OrderedDict  # pylint: disable=unused-argument
        """Metaclass magic for object storage.

        .. versionadded:: 1.2.0
        """
        return collections.OrderedDict()  # pragma: no cover


class Subprocess(six.with_metaclass(SingletonMeta, api.ExecHelper)):
    """Subprocess helper with timeouts and lock-free FIFO."""

    def __init__(
        self,
        log_mask_re=None,  # type: typing.Optional[str]
    ):  # type: (...) -> None
        """Subprocess helper with timeouts and lock-free FIFO.

        For excluding race-conditions we allow to run 1 command simultaneously

        :param log_mask_re: regex lookup rule to mask command for logger.
                            all MATCHED groups will be replaced by '<*masked*>'
        :type log_mask_re: typing.Optional[str]

        .. versionchanged:: 1.2.0 log_mask_re regex rule for masking cmd
        """
        super(Subprocess, self).__init__(logger=logger, log_mask_re=log_mask_re)
        self.__process = None

    def _exec_command(
        self,
        command,  # type: str
        interface,  # type: subprocess.Popen
        stdout,  # type: typing.Optional[typing.IO]
        stderr,  # type: typing.Optional[typing.IO]
        timeout,  # type: typing.Union[int, None]
        verbose=False,  # type: bool
        log_mask_re=None,  # type: typing.Optional[str]
        **kwargs
    ):  # type: (...) -> exec_result.ExecResult
        """Get exit status from channel with timeout.

        :param command: Command for execution
        :type command: str
        :param interface: Control interface
        :type interface: subprocess.Popen
        :param stdout: STDOUT pipe or file-like object
        :type stdout: typing.Any
        :param stderr: STDERR pipe or file-like object
        :type stderr: typing.Any
        :param timeout: Timeout for command execution
        :type timeout: typing.Union[int, None]
        :param verbose: produce verbose log record on command call
        :type verbose: bool
        :param log_mask_re: regex lookup rule to mask command for logger.
                            all MATCHED groups will be replaced by '<*masked*>'
        :type log_mask_re: typing.Optional[str]
        :rtype: ExecResult
        :raises ExecHelperTimeoutError: Timeout exceeded

        .. versionadded:: 1.2.0
        """
        @threaded.threadpooled
        def poll_stdout():
            """Sync stdout poll."""
            result.read_stdout(
                src=stdout,
                log=logger,
                verbose=verbose
            )
            interface.wait()  # wait for the end of execution

        @threaded.threadpooled
        def poll_stderr():
            """Sync stderr poll."""
            result.read_stderr(
                src=stderr,
                log=logger,
                verbose=verbose
            )

        # Store command with hidden data
        cmd_for_log = self._mask_command(cmd=command, log_mask_re=log_mask_re)

        result = exec_result.ExecResult(cmd=cmd_for_log)

        # pylint: disable=assignment-from-no-return
        stdout_future = poll_stdout()  # type: concurrent.futures.Future
        stderr_future = poll_stderr()  # type: concurrent.futures.Future
        # pylint: enable=assignment-from-no-return

        concurrent.futures.wait([stdout_future, stderr_future], timeout=timeout)  # Wait real timeout here
        exit_code = interface.poll()  # Update exit code

        # Process closed?
        if exit_code is not None:
            result.exit_code = exit_code
            return result
        # Kill not ended process and wait for close
        try:
            interface.kill()  # kill -9
            concurrent.futures.wait([stdout_future, stderr_future], timeout=5)
            # Force stop cycle if no exit code after kill
            stdout_future.cancel()
            stderr_future.cancel()
        except OSError:
            exit_code = interface.poll()
            if exit_code is not None:  # Nothing to kill
                logger.warning("{!s} has been completed just after timeout: please validate timeout.".format(command))
                result.exit_code = exit_code
                return result
            raise  # Some other error

        wait_err_msg = _log_templates.CMD_WAIT_ERROR.format(result=result, timeout=timeout)
        logger.debug(wait_err_msg)
        raise exceptions.ExecHelperTimeoutError(result=result, timeout=timeout)

    def execute_async(
        self,
        command,  # type: str
        stdin=None,  # type: typing.Union[typing.AnyStr, bytearray, None]
        open_stdout=True,  # type: bool
        open_stderr=True,  # type: bool
        verbose=False,  # type: bool
        log_mask_re=None,  # type: typing.Optional[str]
        **kwargs
    ):  # type: (...) -> typing.Tuple[subprocess.Popen, None, typing.Optional[typing.IO], typing.Optional[typing.IO], ]
        """Execute command in async mode and return Popen with IO objects.

        :param command: Command for execution
        :type command: str
        :param stdin: pass STDIN text to the process
        :type stdin: typing.Union[typing.AnyStr, bytearray, None]
        :param open_stdout: open STDOUT stream for read
        :type open_stdout: bool
        :param open_stderr: open STDERR stream for read
        :type open_stderr: bool
        :param verbose: produce verbose log record on command call
        :type verbose: bool
        :param log_mask_re: regex lookup rule to mask command for logger.
                            all MATCHED groups will be replaced by '<*masked*>'
        :type log_mask_re: typing.Optional[str]
        :rtype: typing.Tuple[
            subprocess.Popen,
            None,
            typing.Optional[typing.IO],
            typing.Optional[typing.IO],
        ]

        .. versionadded:: 1.2.0
        """
        cmd_for_log = self._mask_command(cmd=command, log_mask_re=log_mask_re)

        self.logger.log(
            level=logging.INFO if verbose else logging.DEBUG,
            msg=_log_templates.CMD_EXEC.format(cmd=cmd_for_log)
        )

        process = subprocess.Popen(
            args=[command],
            stdout=subprocess.PIPE if open_stdout else devnull,
            stderr=subprocess.PIPE if open_stderr else devnull,
            stdin=subprocess.PIPE,
            shell=True,
            cwd=kwargs.get('cwd', None),
            env=kwargs.get('env', None),
            universal_newlines=False,
        )

        if stdin is not None:
            if isinstance(stdin, six.text_type):
                stdin = stdin.encode(encoding='utf-8')
            elif isinstance(stdin, bytearray):
                stdin = bytes(stdin)
            try:
                process.stdin.write(stdin)
            except OSError as exc:
                if exc.errno == errno.EINVAL:
                    # bpo-19612, bpo-30418: On Windows, stdin.write() fails
                    # with EINVAL if the child process exited or if the child
                    # process is still running but closed the pipe.
                    self.logger.warning('STDIN Send failed: closed PIPE')
                elif exc.errno in (errno.EPIPE, errno.ESHUTDOWN):  # pragma: no cover
                    self.logger.warning('STDIN Send failed: broken PIPE')
                else:
                    process.kill()
                    raise
            try:
                process.stdin.close()
            except OSError as exc:
                if exc.errno in (errno.EINVAL, errno.EPIPE, errno.ESHUTDOWN):
                    pass
                else:
                    process.kill()
                    raise

        return process, None, process.stderr, process.stdout
