from logging import *

rootLogger = getLogger()
rootLogger.addHandler(NullHandler())
rootLogger.setLevel(DEBUG)

class RawStreamHandler(StreamHandler):
    """Exactly like logging.StreamHandler except it doesn't add
    a trailing newline to messages before writing to the stream
    (this works better with the carriage returns we use in output)"""
    def emit(self, record):
        message = record.getMessage()
        self.stream.write(message)
        self.flush()
        