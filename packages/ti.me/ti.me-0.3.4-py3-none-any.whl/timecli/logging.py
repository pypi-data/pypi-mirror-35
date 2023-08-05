import logging
from os import (
    path,
    makedirs,
)
from logging import getLogger
from functools import wraps

import timelib.logging
from timecli.config import (
    LOGGING_PATH,
    LOGLEVEL,
    LIB_LOGFILE,
    CLI_LOGFILE,
)


def init_logging(loglevel=LOGLEVEL, logging_path=LOGGING_PATH):
    makedirs(logging_path, exist_ok=True)

    liblogger = timelib.logging.get_logger()
    libhandler = logging.FileHandler(path.join(
        logging_path,
        LIB_LOGFILE,
    ))

    liblogger.setLevel(loglevel)
    liblogger.addHandler(libhandler)

    clilogger = get_logger()
    clihandler = logging.FileHandler(path.join(
        logging_path,
        CLI_LOGFILE,
    ))

    clilogger.setLevel(loglevel)
    clilogger.addHandler(clihandler)


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_logger()
        logger.info(f'Call {func.__name__}')
        logger.debug(f'args: {args}')
        logger.debug(f'kwargs: {kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.debug(f'result: {result}')
            return result
        except Exception as e:
            logger.exception(e)
            raise
    return wrapper


def get_logger():
    return getLogger('timecli')
