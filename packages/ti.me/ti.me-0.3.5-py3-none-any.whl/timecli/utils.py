from tempfile import mkstemp
from os import (
    makedirs,
    getenv,
)
from pathlib import Path
import json
import subprocess

from timecli.logging import logged
from timecli.config import (
    CONFIG_PATH,
    LOGGING_PATH,
    STORAGE_URL,
    USER,
    LOGLEVEL,
    WARNFILTER,
    TIME_FORMAT,
)


@logged
def gettext():
    (_, path) = mkstemp()
    editor = getenv('EDITOR', 'vi')
    retcode = subprocess.call(f'{editor} {path}', shell=True)
    if retcode == 0:
        with open(path, 'r') as f:
            return f.read()
    raise ValueError(f'Editor terminated with {retcode} return code')


@logged
def init_config(
    config_path=CONFIG_PATH,
    storage_url=STORAGE_URL,
    logging_path=LOGGING_PATH,
    user=USER,
    loglevel=LOGLEVEL,
    warnfilter=WARNFILTER,
    time_format=TIME_FORMAT,
):
    makedirs(Path(config_path).parents[0], exist_ok=True)
    with open(config_path, 'w') as file:
        json.dump({
            'user': user,
            'storage': storage_url,
            'logging': logging_path,
            'loglevel': loglevel,
            'warnfilter': warnfilter,
            'timeformat': time_format,
        }, file, sort_keys=True, indent=2)
        file.write('\n')


@logged
def stringify_relativedelta(value):
    string = ' '.join(
        f'{value} {key}'
        for key, value
        in {
            'years': value.years,
            'months': value.months,
            'weeks': value.weeks,
            'days': value.days,
            'hours': value.hours,
            'minutes': value.minutes,
            'seconds': value.seconds,
        }.items()
        if value
    )

    if not string:
        string = '0 hours'

    return string
