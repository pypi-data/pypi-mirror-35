# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# author: clarkmatthew
# modified by: Trevor Hodde

'''
    Example:
    import eulogger
    self.logger = eulogger.Eulogger(name='euca')
    self.log = self.logger.log

    self.debug("This is a debug message")
    self.critical("this is a critical message")
'''

import os
import sys
import logging
import time


class Eulogger(logging.Logger):
    # constructor for the Eulogger

    def __init__(self,
                 identifier,
                 parent_logger_name='eulogger',
                 stdout_level="debug",
                 stdout_format=None,
                 logfile="",
                 logfile_level="INFO",
                 file_format=None,
                 show_init=False):
        """
        This class basically sets up a child debugger for testing purposes.
        It allows the user to set up a new logger object and pass different logging formats and
        levels so different objects and modules can log with unique identifiers and logging levels.


        :param parent_logger_name: Name of root/parent logger
        :param identifier: identifier used for log formatting and child logger name
        :param stdout_level: log level (see 'logging' class) for std out handler under this
                             child logger
        :param stdout_format: logging format used by this child logger's stdout handler
        :param logfile: file path to use for this child logger's logging file handler
        :param logfile_level: log level (see 'logging' class) for file handler under this
                              child logger
        :param file_format: logging formate used by this child logger's file handler
        :param clear_file: will attempt to remove 'logfile' before creating handler. Will not
                           remove parent's files.
        :param make_log_file_global: boolean, will add this logfile to parent so other child
                                     loggers create afterward will attempt to create a handler
                                      that writes to this file as well.
        :param use_global_log_files: boolean, will query the parent logger for any file handlers
                                     and will attempt to create a handler for this child logger
                                     using the same file
        """
        # Debug for init...
        if show_init:
            print ('-----------------------------------------------\n'
                   'parent_logger_name:{0}\neulogger init:\nidentifier:{1}\nstdout_level:{2}\n'
                   'stdout_format:{3}\nlogfile:{4}\nlogfile_level:{5}\nfile_format:{6}\n'
                   '\n-----------------------------------------------'
                   .format(parent_logger_name, identifier, stdout_level, stdout_format, logfile,
                           logfile_level, file_format))
        # Create or fetch existing logger of name 'logger_name
        if isinstance(stdout_level, basestring):
            self.stdout_level = getattr(logging, stdout_level.upper(), logging.DEBUG)
        elif isinstance(stdout_level, int):
            self.stdout_level = stdout_level
        else:
            self.stdout_level = logging.DEBUG
        if isinstance(logfile_level, basestring):
            self.logfile_level = getattr(logging, logfile_level.upper(), logging.DEBUG)
        else:
            self.logfile_level = logfile_level or logging.DEBUG
        self.parent_logger_name = parent_logger_name
        # Create a logger
        self.identifier = identifier
        name = str(identifier).replace(".", ":")
        self.name = "{0}.{1}".format(self.parent_logger_name, name)


        parent_logger = logging.getLogger(self.parent_logger_name)
        self.parent = parent_logger
        if hasattr(parent_logger, 'getChild'):
            childlogger = parent_logger.getChild(name)
        else:
            childlogger = self._getChild(parent_logger, name)
        if childlogger:
            self.__dict__.update(childlogger.__dict__)

        self.logfile = os.path.join(logfile)
        self._default_format = stdout_format or logging.Formatter(
            '[%(asctime)s][%(levelname)s]%(message)s')
        self.file_format = file_format or self._default_format

        # Add handler for stdout...
        stdout_handler = None
        for handler in self.parent.handlers:
            if isinstance(handler, logging.StreamHandler):
                if 'stdout' in handler.stream.name:
                    stdout_handler = handler
        if not stdout_handler:
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(self._default_format)
            stdout_handler.setLevel(self.stdout_level)
            self.parent.addHandler(stdout_handler)
            self.parent.setLevel(self.stdout_level)
        self.stdout_handler = stdout_handler

        # Now add the file handlers...
        file_info_list = self.getparent_files()
        if self.logfile:
            self.logfile = os.path.abspath(self.logfile)
            if self.logfile not in file_info_list:
                file_hdlr = logging.FileHandler(self.logfile)
                file_hdlr.setFormatter(self._default_format)
                file_hdlr.setLevel(logfile_level)
                self.parent.addHandler(file_hdlr)
        self.manager.loggerDict[self.name] = self

    def _log(self, level, msg, args, exc_info=None, extra=None):
        msg = "[{0}]: {1}".format(self.identifier, msg)
        try:
            return super(Eulogger, self)._log(level, msg, args, exc_info=exc_info, extra=extra)
        except TypeError:
            return logging.Logger._log(self, level, msg, args, exc_info=exc_info, extra=extra)

    def getparent_files(self):
        files = []
        if self.parent:
            for h in self.parent.handlers:
                if isinstance(h, logging.FileHandler):
                    files.append(h.stream.name)
        return files

    def set_stdout_loglevel(self, level):
        if not isinstance(level, int) and isinstance(level, basestring):
            level = getattr(logging, level.upper())
        self.setLevel(level)
        for handler in self.handlers:
            if 'stdout' in handler.stream.name:
                handler.setLevel(level)
        if self.parent:
            self.parent.setLevel(level)
            for handler in self.parent.handlers:
                if 'stdout' in handler.stream.name:
                    handler.setLevel(level)
        self.stdout_level = level

    @staticmethod
    def _getChild(logger, suffix):
        func = getattr(logging.Logger, 'getChild', None)
        if func:
            return func(logger, suffix)
        else:
            if logger.root is not logger:
                suffix = '.'.join((logger.name, suffix))
            return logger.manager.getLogger(suffix)

    def getChild(self, suffix):
        return self._getChild(self, suffix)

    @classmethod
    def format_log_level(self, level, default=logging.DEBUG):
        if isinstance(level, basestring):
            return getattr(logging, level.upper(), default)
        if isinstance(level, int):
            return level
        return default

    def close(self):
        for handler in self.handlers:
            try:
                handler.close()
            except Exception as CE:
                self.log.warning('Could not close log handler, err:"{0}"'.format(CE))


class AllowLoggerByName(logging.Filter):
    """
    Only messages from this logger are allow through to prevent duplicates from other
    loggers of same level, etc..
    """
    def __init__(self, name=""):
        logging.Filter.__init__(self, name)

    def filter(self, record):
        return record.name == self.name


class MuteFilter(logging.Filter):
    def filter(self, record):
        return False
