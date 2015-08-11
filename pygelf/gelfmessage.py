import logging


_levels = {
    logging.DEBUG: 7,
    logging.INFO: 6,
    logging.WARNING: 4,
    logging.ERROR: 3,
    logging.CRITICAL: 2
}


class GelfMessage:

    def __init__(self, record, debug):
        self.version = '1.1'
        self.short_message = record.message
        self.full_message = record.exc_text
        self.timestamp = record.created
        self.level = _levels[record.levelno]

        if debug:
            self._file = record.filename
            self._line = record.lineno
            self._module = record.module
            self._func = record.funcName
