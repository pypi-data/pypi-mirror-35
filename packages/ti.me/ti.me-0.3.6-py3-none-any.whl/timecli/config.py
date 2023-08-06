from os import (
    path,
    environ,
)
from getpass import getuser
import locale


ENVIRONMENT_PATH = path.join(environ['HOME'], '.ti.me')
CONFIG_PATH = path.join(ENVIRONMENT_PATH, 'config.json')
LOGGING_PATH = path.join(ENVIRONMENT_PATH, 'log')
STORAGE_URL = f'sqlite:///{path.join(ENVIRONMENT_PATH, "storage.sqlite")}'
USER = getuser()
LOGLEVEL = 'INFO'
WARNFILTER = 'ignore'
LIB_LOGFILE = 'timelib.log'
CLI_LOGFILE = 'timecli.log'
TIME_FORMAT = locale.nl_langinfo(locale.D_T_FMT)
