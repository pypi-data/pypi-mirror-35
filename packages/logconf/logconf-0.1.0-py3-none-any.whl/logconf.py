from __future__ import absolute_import
from json import dumps as json_dumps
import contextlib
import logging
import logging.handlers
import sys
import time

__all__ = ['logconf']

LOG = logging.getLogger(__name__)


class JsonFormatter(logging.Formatter):
    """
    Formatter for writing line-delimited JSON logs.
    """
    _special_fields = ('msg', 'isotime', 'asctime', 'args')
    default_fields = ('levelname', 'name', 'msg', 'isotime')
    separators = (',', ':')

    def __init__(self, fields=None, datefmt=None):
        super(JsonFormatter, self).__init__(datefmt=datefmt)
        self.fields = set(fields or self.default_fields)

    def format(self, record):
        data = {}

        if 'msg' in self.fields:
            record.message = record.getMessage()
            data['msg'] = self.formatMessage(record)

        if 'isotime' in self.fields:
            data['isotime'] = time.strftime(
                '%Y-%m-%dT%H:%M:%S%z',
                self.converter(record.created),
            )

        if 'asctime' in self.fields:
            data['asctime'] = self.formatTime(record)

        if record.exc_info and not record.exc_text:
            record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            data['exc_info'] = record.exc_text

        if record.stack_info and 'stack_info' in self.fields:
            data['stack_info'] = self.formatStack(record.stack_info)

        for key in self.fields:
            if key not in data and key not in self._special_fields:
                data[key] = getattr(record, key)

        return json_dumps(data, separators=self.separators)
    
    def __repr__(self):
        return 'JsonFormatter(keys=[%s])' % ','.join(self.fields)


def get_formatter(colors, shortened_levels=True):
    level_len = 5 if shortened_levels else 8
    if colors:
        level_len += 11
        fmt = '\033[37m%(asctime)s %(levelname_colored)' + str(level_len) + \
            's\033[37m %(name)s \033[0m%(message)s'
    else:
        fmt = '%(asctime)s [%(levelname)' + str(level_len) + 's] [%(name)s] %(message)s'
    return logging.Formatter(fmt)


class ColorLogRecord(logging.LogRecord):
    RESET = '\033[0m'
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = (
        '\033[1;%dm' % (i + 30) for i in range(8)
    )

    COLORS = {
        logging.DEBUG: GREEN,
        logging.INFO: BLUE,
        logging.WARNING: MAGENTA,
        logging.ERROR: YELLOW,
        logging.CRITICAL: RED,
    }

    def __init__(self, *args, **kwargs):
        super(ColorLogRecord, self).__init__(*args, **kwargs)
        self.levelname_colored = ''.join((
            self.COLORS[self.levelno],
            self.levelname,
            self.RESET,
        ))


def _shorten_levels():
    #pylint: disable=no-member,protected-access
    if hasattr(logging, '_levelNames'):
        # python 2.7, 3.3
        logging._levelNames[logging.WARNING] = 'WARN'
        logging._levelNames['WARN'] = logging.WARNING
        logging._levelNames[logging.CRITICAL] = 'CRIT'
        logging._levelNames['CRIT'] = logging.CRITICAL
    else:
        # python 3.4+
        logging._levelToName[logging.WARNING] = 'WARN'
        logging._nameToLevel['WARN'] = logging.WARNING
        logging._levelToName[logging.CRITICAL] = 'CRIT'
        logging._nameToLevel['CRIT'] = logging.CRITICAL
    #pylint: enable=no-member,protected-access


def normalize_level(level):
    if level is None:
        return logging.NOTSET
    if isinstance(level, (str, bytes)):
        return logging.getLevelName(level.upper())
    return level


class LogSetup:
    """
    Class that makes it easy to set up many different types of loggers.

    ls = LogSetup()
    ls.add_file('/var/log/myapp.log', logging.WARNING)
    ls.add_file('/var/log/myapp-debug.log', logging.DEBUG)
    ls.add_console(logging.INFO)
    ls.finish()
    """
    def __init__(self, *, logger_name='', level=logging.NOTSET,
                 handler_level=logging.NOTSET,
                 colors=False, shorten_levels=False):
        """
        Args:
            logger_name: Name of the logger to start configuring at.
            level: Which level to set on the root logger. If this is set,
                levels lower than this will be ignored even if set on individual
                handlers, so it's usually a good idea to leave this at NOTSET.
            handler_level: Which level to set for handlers by default.
            colors: Use colors in console logging if possible.
            shorten_levels: Shorten long log level names.
        """
        self.logger_name = logger_name
        self.level = level
        self.is_root = logger_name == ''
        self.handler_level = handler_level
        self.colors = colors
        self.shorten_levels = shorten_levels
        self.startup_messages = []
        self.handlers = []

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, level):
        self._level = normalize_level(level)

    @property
    def handler_level(self):
        return self._handler_level
    
    @handler_level.setter
    def handler_level(self, level):
        self._handler_level = normalize_level(level)

    def add_startup_message(self, level, message, *args):
        """
        Add a line to be logged once logging has been set up.
        """
        self.startup_messages.append((level, message) + args)

    def add_file(self, file, level=None, json=False, json_fields=None):
        """
        Log to a file.
        """
        if file.lower() == 'stderr':
            handler = logging.StreamHandler(sys.stderr)
            file = 'STDERR'
        elif file.lower() == 'stdout':
            handler = logging.StreamHandler(sys.stdout)
            file = 'STDOUT'
        elif file:
            handler = logging.handlers.WatchedFileHandler(file)

        if json:
            formatter = JsonFormatter(fields=json_fields)
        else:
            # define the logging format
            formatter = get_formatter(
                colors=self.colors and file in ('STDERR', 'STDOUT'),
                shortened_levels=self.shorten_levels,
            )
        handler.setFormatter(formatter)

        if level is None:
            level = self.handler_level
        else:
            level = normalize_level(level)
        handler.setLevel(level)

        self.add_startup_message(
            logging.INFO,
            'setting up log handler %r to %s with level %s',
            handler, file, level,
        )
        self.handlers.append(handler)

    def add_json(self, file, level=None, fields=None):
        """
        Log in JSON format to a file.
        """
        self.add_file(file, level=level, json=True, json_fields=fields)

    def add_console(self, level=None, check_interactive=True):
        """
        Log to the console/terminal.
        Args:
            level: The log level.
            check_interactive: If True, checks if stderr is a TTY, and only sets
                up logging if it is.
        """
        if check_interactive and not sys.__stderr__.isatty(): #pylint: disable=no-member
            self.add_startup_message(
                logging.INFO,
                'sys.stderr is not a TTY, not logging to it',
            )
            return
        self.add_file('stderr', level=level)

    def finish(self):
        """
        Complete logging setup.
        """
        if self.is_root:
            if self.shorten_levels:
                _shorten_levels()

            if self.colors:
                if hasattr(logging, 'setLogRecordFactory'):
                    logging.setLogRecordFactory(ColorLogRecord) #pylint: disable=no-member
                else:
                    self.add_startup_message(
                        logging.WARNING,
                        'color logging not supported in python2, sorry',
                    )

        root = logging.getLogger(self.logger_name)
        root.setLevel(self.level)

        for handler in self.handlers:
            root.addHandler(handler)

        for line in self.startup_messages:
            level, message = line[:2]
            args = line[2:]
            LOG.log(level, message, *args)

    def logger(self, logger_name, **kwargs):
        if not self.is_root:
            raise RuntimeError('can only call logger() on root!')

        kwargs.setdefault('level', self.level)
        kwargs.setdefault('colors', self.colors)
        return type(self)(logger_name)


@contextlib.contextmanager
def logconf(*args, **kwargs):
    lc = LogSetup(*args, **kwargs)
    yield lc
    lc.finish()
