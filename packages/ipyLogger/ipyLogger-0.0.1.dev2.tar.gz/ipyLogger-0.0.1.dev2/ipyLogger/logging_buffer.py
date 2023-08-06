from .logger import get_logger as get_logger_


class BufferManager():
    def __init__(self):
        self.current_LoggingBuffer = None

    def get_current_log_buffer(self):
        if self.current_LoggingBuffer is None:
            self.current_LoggingBuffer = LoggingBuffer()
        return self.current_LoggingBuffer


MANAGER = BufferManager()


def get_logger(env, loglevel=None,**kwargs):
    if loglevel is None:
        logging_buffer = MANAGER.get_current_log_buffer()
        return get_logger_(env, logging_buffer.level,**kwargs)
    else:
        return get_logger_(env, loglevel,**kwargs)

# to extend with other options if necessary
class LoggingBuffer():
    def __init__(self, verbose=True, debug=False):
        if debug:
            self.level = 'DEBUG'
        elif verbose:
            self.level = 'INFO'
        else:
            self.level = 'CRITICAL'

        MANAGER.current_LoggingBuffer = self


def mute_logger():
    LoggingBuffer(verbose=False)

def activate_debug():
    LoggingBuffer(debug=True)

def enable_log():
    LoggingBuffer(verbose=True)