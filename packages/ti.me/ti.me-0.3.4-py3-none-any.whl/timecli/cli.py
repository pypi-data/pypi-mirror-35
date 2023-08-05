from os import path
import sys
import json
import warnings

from timelib import (
    create_session,
    Manager,
)
from timelib.exceptions import (
    TimeLibError,
    TimeLibWarning,
)
from timecli.config import (
    CONFIG_PATH,
    LOGGING_PATH,
    STORAGE_URL,
    USER,
    LOGLEVEL,
    WARNFILTER,
    TIME_FORMAT,
)
from timecli.logging import (
    init_logging,
    get_logger,
)
from timecli.parsing import create_parser
from timecli.handling import root_handle
from timecli.utils import init_config


def main():
    args = create_parser().parse_args()

    config_path = args.config or CONFIG_PATH

    if not path.isfile(config_path):
        init_config(config_path=config_path)

    with open(config_path, 'r') as file:
        config = json.load(file)

    config = {
        'user': args.user or config.get('user', USER),
        'storage': args.storage or config.get('storage', STORAGE_URL),
        'logging': args.logging or config.get('logging', LOGGING_PATH),
        'loglevel': args.loglevel or config.get('loglevel', LOGLEVEL),
        'warnfilter': args.warnfilter or config.get('warnfilter', WARNFILTER),
        'timeformat': config.get('timeformat', TIME_FORMAT),
    }

    warnings.filterwarnings(config['warnfilter'])

    init_logging(
        loglevel=config['loglevel'],
        logging_path=config['logging'],
    )

    get_logger().debug(f'args: {args}')
    get_logger().debug(f'config: {config}')

    manager = Manager(
        session=create_session(config['storage']),
        default_user=config['user'],
    )

    try:
        root_handle(manager, args, config['timeformat'])
    except TimeLibError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except TimeLibWarning as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception:
        print('Internal error. See log for more details', file=sys.stderr)
        sys.exit(1)
