from logging import getLogger
from functools import wraps


def logged(func):
    """Wraps given function with logging."""
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
    """Returns library logger."""
    return getLogger('timelib')
