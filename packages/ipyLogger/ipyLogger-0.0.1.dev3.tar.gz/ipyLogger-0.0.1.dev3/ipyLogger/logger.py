__author__ = 'echo5india'

import threading
import logging
import six

from ipywidgets import widgets
from IPython.display import display_html

from toolz.functoolz import memoize
import logging.handlers
import sys

_LOCK = threading.Lock()


@memoize
def _get_logger(env, loglevel, ipython_cell_number=None, **kwargs):
    """
    Instantiate logger singletons
    Args:
        env (str): "dev", "uat" etc
    Returns:
        AsyncLogger
    """

    # logging.setLoggerClass(AsyncLogger)
    logger_name = '{}.{}'.format(ipython_cell_number, env) if ipython_cell_number else '{}'.format(env)
    logger = logging.getLogger(logger_name)
    logging.setLoggerClass(logging.Logger)
    logger.setLevel(loglevel)

    # Clean existing handlers
    for hdlr in logger.handlers:
        logger.removeHandler(hdlr)

    console = WidgetHandler(**kwargs)
    logger.addHandler(console)

    # Avoid leaking out to parent
    logger.propagate = False

    return logger


def get_logger(env='', loglevel='INFO', **kwargs):
    """
    :param: env : str : name of the logger environment
    Returns a logger for the current env, logging level and service logging level
    Returns:
        logging.Logger:  appropriate to current env.
    """

    if is_in_ipython():
        current_cell_nb = len(sys.modules['__main__'].__dict__['In']) - 1
        log = _get_logger(env, loglevel, current_cell_nb, **kwargs)
    else:
        log = _get_logger(env, loglevel, **kwargs)

    return log


# class AsyncLogger(logging.Logger):
#
#     def __init__(self, name, level=logging.NOTSET):
#         super(AsyncLogger, self).__init__(name, level)
#         self.listener = None
#         self.old_handlers = []
#
#     def start_async(self):
#         """
#         Set the given logger with an asynchronous handler
#         """
#         log_queue = queue.Queue(-1)  # no limit on size
#         self.listener = QueueListener(log_queue, *self.handlers)
#         self.old_handlers = self.handlers
#         self.handlers = [QueueHandler(log_queue)]
#         self.listener.start()
#
#     def stop_async(self):
#         """
#         Restore the logger's handlers & stop the listner
#         """
#         self.listener.stop()
#         self.handlers = self.old_handlers


def get_ipython_func():
    return sys.modules['__main__'].__dict__.get('get_ipython', None)


def is_in_ipython():
    get_ipython = get_ipython_func()
    if get_ipython is None:
        return False
    else:
        return get_ipython() is not None


class WidgetHandler(logging.Handler):
    def __init__(self, **kwargs):
        logging.Handler.__init__(self)
        self._console_cached = None
        formatter = kwargs.pop('formatter', ' %(name)s | %(asctime)s | %(levelname)s:  %(message)s')
        self.setFormatter(logging.Formatter(formatter))

    def _console(self):
        """Lazy console initialization, avoid display on start
        """
        with _LOCK:
            if self._console_cached is None:
                self._console_cached = WidgetConsole()
                self._console_cached.display()
            return self._console_cached

    def emit(self, record):
        """ Overload of logging.Handler method """

        try:
            self._console().writeln(self.format(record))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def show_logs(self):
        """ Show the logs """
        # display(self.out)
        self._console_cached.display()


class BaseWidget(object):
    """
    """

    def __init__(self, obj):
        self._obj = obj

    @property
    def widget(self):
        return self._obj

    def set_layout(self, **x):
        for k, v in six.iteritems(x):
            setattr(self.widget.layout, k, v)

    def display(self):
        from IPython.display import display
        display(self._obj)


class WidgetConsole(BaseWidget):
    """
    """

    def __init__(self, layout=None):
        self._data = ""

        self.display_html = display_html
        super(WidgetConsole, self).__init__(widgets.Textarea())
        layout_to_use = {'color': '#000088',
                         'background': '#eeeeee',
                         'width': '100%',
                         'height': '200px',
                         'border': '1px solid #999999'}
        if layout:
            layout_to_use.update(layout)

        self.set_layout(**layout_to_use)

    def flush(self):
        self._data = ""

    def writeln(self, x):
        self.write(x.rstrip() + '\n')

    def write(self, x):
        self._data += x
        self._obj.value = self._data
