import sys
import re
import argparse

import dateutil.parser
from dateutil.relativedelta import relativedelta

from timelib.models import TaskPriority
from timecli.logging import logged


class ArgumentParser(argparse.ArgumentParser):
    @logged
    def error(self, message):
        print(f'error: {message}', file=sys.stderr)
        self.print_help()
        sys.exit(2)


@logged
def parse_priority(string):
    return TaskPriority[string.upper()]


@logged
def parse_bool(string):
    if string.lower() in ['yes', 'true', 't', 'y', '1']:
        return True
    if string.lower() in ['no', 'false', 'f', 'n', '0']:
        return False
    raise ValueError('Invalid bool format')


@logged
def parse_relativedelta(string):
    if re.match(
        (
            r'([+-]?\d+) (years|months|weeks|days|hours|minutes|seconds)'
            r'(,\s*([+-]?\d+)'
            r' (years|months|weeks|days|hours|minutes|seconds))*'
        ),
        string,
    ):
        return relativedelta(**{
            key: int(value)
            for value, key
            in re.findall(
                r'([+-]?\d+) (years|months|weeks|days|hours|minutes|seconds)',
                string,
            )
        })

    raise ValueError(f'Invalid delta format')


def configure_task_parser(subject_action):
    task_parser = subject_action.add_parser('task', description='manage tasks')
    command_action = task_parser.add_subparsers(
        dest='command',
        help='action with tasks',
    )
    command_action.required = True

    add_parser = command_action.add_parser('add', description='create task')
    add_parser.add_argument('text', nargs='?', help='task description')
    add_parser.add_argument(
        '-f',
        '--from',
        type=dateutil.parser.parse,
        help='task begin time',
    )
    add_parser.add_argument(
        '-t',
        '--to',
        type=dateutil.parser.parse,
        help='task end time',
    )
    add_parser.add_argument(
        '-p',
        '--priority',
        type=parse_priority,
        help='task priority',
    )
    add_parser.add_argument(
        '-bt',
        '--blocking-tasks',
        nargs='+',
        type=int,
        help='tasks that block this task',
    )
    add_parser.add_argument(
        '-tt',
        '--target-tasks',
        nargs='+',
        type=int,
        help='tasks that are triggered with this task',
    )
    add_parser.add_argument('-l', '--labels', nargs='+', help='task labels')
    add_parser.add_argument(
        '-m',
        '--members',
        nargs='+',
        help='task members (implicitly including user)',
    )

    edit_parser = command_action.add_parser('edit', description='edit task')
    edit_parser.add_argument('id', type=int, help='task id')
    edit_parser.add_argument('--text', help='new description')
    edit_parser.add_argument(
        '-f',
        '--from',
        type=dateutil.parser.parse,
        help='new begin time',
    )
    edit_parser.add_argument(
        '-t',
        '--to',
        type=dateutil.parser.parse,
        help='new end time',
    )
    edit_parser.add_argument(
        '-p',
        '--priority',
        type=parse_priority,
        help='new priority',
    )
    edit_parser.add_argument(
        '-c',
        '--completed',
        type=parse_bool,
        help='new completed flag',
    )
    edit_parser.add_argument(
        '-a',
        '--archived',
        type=parse_bool,
        help='new archived flag',
    )
    edit_parser.add_argument(
        '-bt',
        '--blocking-tasks',
        nargs='*',
        type=int,
        help=f'new blocking tasks list (see "{add_parser.prog} -h")',
    )
    edit_parser.add_argument(
        '-tt',
        '--target-tasks',
        nargs='*',
        type=int,
        help=f'new target tasks list (see "{add_parser.prog} -h")',
    )
    edit_parser.add_argument(
        '-l',
        '--labels',
        nargs='*',
        help='new labels list',
    )
    edit_parser.add_argument(
        '-m',
        '--members',
        nargs='*',
        help='new members list (implicitly including user)',
    )

    list_parser = command_action.add_parser(
        'list',
        description='show tasks in compact way',
    )
    list_parser.add_argument(
        '-a',
        '--archived',
        type=parse_bool,
        help='archived flag filter',
    )
    list_parser.add_argument(
        '-c',
        '--completed',
        type=parse_bool,
        help='completed flag filter',
    )
    list_parser.add_argument(
        '-l',
        '--labels',
        nargs='+',
        help='labels filter'
        ' (show tasks that contains in all specified labels)',
    )

    delete_parser = command_action.add_parser(
        'delete',
        description='delete task',
    )
    delete_parser.add_argument('id', type=int, help='task id')

    show_parser = command_action.add_parser(
        'show',
        description='show specified task',
    )
    show_parser.add_argument('id', type=int, help='task id')

    complete_parser = command_action.add_parser(
        'complete',
        description='complete task',
    )
    complete_parser.add_argument('id', type=int, help='task id')

    archive_parser = command_action.add_parser(
        'archive',
        description='archive task',
    )
    archive_parser.add_argument('id', type=int, help='task id')

    block_parser = command_action.add_parser(
        'block',
        description='block task with other',
    )
    block_parser.add_argument('id', type=int, help='task id')
    block_parser.add_argument(
        'blocking',
        type=int,
        help=f'blocking task (see "{add_parser.prog} -h")',
    )

    target_parser = command_action.add_parser(
        'target',
        description='set trigger target for task',
    )
    target_parser.add_argument('id', type=int, help='task id')
    target_parser.add_argument(
        'target',
        type=int,
        help=f'target task (see "{add_parser.prog} -h")',
    )

    share_parser = command_action.add_parser('share', description='share task')
    share_parser.add_argument('id', type=int, help='task id')
    share_parser.add_argument('members', nargs='+', help='users to share')


def configure_planned_task_parser(subject_action):
    planned_task_parser = subject_action.add_parser(
        'planned-task',
        description='manage planned tasks',
    )
    command_action = planned_task_parser.add_subparsers(
        dest='command',
        help='action with planned task',
    )
    command_action.required = True

    add_parser = command_action.add_parser(
        'add',
        description='create planned task',
    )
    add_parser.add_argument('plan', type=int, help='plan for task')
    add_parser.add_argument('text', nargs='?', help='task description')
    add_parser.add_argument(
        '-f',
        '--from',
        type=parse_relativedelta,
        help=(
            'task begin time related on creation time'
            ' (ex: 1 weeks 12 hours 2 days)'
        ),
    )
    add_parser.add_argument(
        '-t',
        '--to',
        type=parse_relativedelta,
        help=(
            'task end time related on creation time'
            ' (ex: 1 weeks 12 hours 2 days)'
        ),
    )
    add_parser.add_argument(
        '-p',
        '--priority',
        type=parse_priority,
        help='task priority',
    )
    add_parser.add_argument(
        '-bt',
        '--blocking-tasks',
        nargs='+',
        type=int,
        help='planned tasks that block this task',
    )
    add_parser.add_argument(
        '-tt',
        '--target-tasks',
        nargs='+',
        type=int,
        help='planned tasks that are triggered with this task',
    )
    add_parser.add_argument('-l', '--labels', nargs='+', help='task labels')
    add_parser.add_argument(
        '-m',
        '--members',
        nargs='+',
        help='task members (implicitly including user)',
    )

    edit_parser = command_action.add_parser('edit')
    edit_parser.add_argument('id', type=int, help='task id')
    edit_parser.add_argument('-t', '--text', help='new description')
    edit_parser.add_argument(
        '-f',
        '--from',
        type=parse_relativedelta,
        help='new relative begin time (ex: 1 weeks 12 hours 2 days)',
    )
    edit_parser.add_argument(
        '-to',
        '--to',
        type=parse_relativedelta,
        help='new relative end time (ex: 1 weeks 12 hours 2 days)',
    )
    edit_parser.add_argument(
        '-p',
        '--priority',
        type=parse_priority,
        help='new priority',
    )
    edit_parser.add_argument(
        '-a',
        '--archived',
        type=parse_bool,
        help='new archived flag with which task will be created',
    )
    edit_parser.add_argument(
        '-c',
        '--completed',
        type=parse_bool,
        help='new completed flag with which task will be created',
    )
    edit_parser.add_argument(
        '-bt',
        '--blocking-tasks',
        nargs='*',
        type=int,
        help=f'new blocking planned tasks list (see "{add_parser.prog} -h")',
    )
    edit_parser.add_argument(
        '-tt',
        '--target-tasks',
        nargs='*',
        type=int,
        help=f'new target planned tasks list (see "{add_parser.prog} -h")',
    )
    edit_parser.add_argument(
        '-l',
        '--labels',
        nargs='*',
        help='new labels list',
    )
    edit_parser.add_argument(
        '-m',
        '--members',
        nargs='*',
        help='new members list (implicitly including user)',
    )

    list_parser = command_action.add_parser(
        'list',
        description='show planned tasks in compact way',
    )
    list_parser.add_argument(
        '-p',
        '--plan',
        type=int,
        help='plan filter (show tasks from specified plan)',
    )
    list_parser.add_argument(
        '-a',
        '--archived',
        type=parse_bool,
        help='archived flag filter',
    )
    list_parser.add_argument(
        '-c',
        '--completed',
        type=parse_bool,
        help='completed flag filter',
    )
    list_parser.add_argument(
        '-l',
        '--labels',
        nargs='+',
        help='labels filter'
        ' (show tasks that contains in all specified labels)',
    )

    delete_parser = command_action.add_parser(
        'delete',
        description='delete planned task',
    )
    delete_parser.add_argument('id', type=int, help='task id')

    show_parser = command_action.add_parser(
        'show',
        description='show specified task',
    )
    show_parser.add_argument('id', type=int, help='task id')


def configure_plan_parser(subject_action):
    plan_parser = subject_action.add_parser('plan', description='manage plans')
    command_action = plan_parser.add_subparsers(
        dest='command',
        help='action with plans',
    )
    command_action.required = True

    add_parser = command_action.add_parser('add', description='create plan')
    add_parser.add_argument(
        'delta',
        type=parse_relativedelta,
        help=(
            'relative time between plan triggerings'
            ' (ex: 1 weeks 12 hours 2 days)'
        ),
    )
    add_parser.add_argument(
        '-f',
        '--from',
        type=dateutil.parser.parse,
        help='plan begin time',
    )
    add_parser.add_argument(
        '-t',
        '--to',
        type=dateutil.parser.parse,
        help='plan end time',
    )
    add_parser.add_argument(
        '-c',
        '--count',
        type=int,
        help='number of plan triggerings',
    )

    edit_parser = command_action.add_parser('edit', description='edit plan')
    edit_parser.add_argument('id', type=int, help='plan id')
    edit_parser.add_argument(
        '-d',
        '--delta',
        type=parse_relativedelta,
        help=(
            f'new plan delta (see {add_parser.prog} -h)'
            f' (ex: 1 weeks 12 hours 2 days)'
        ),
    )
    edit_parser.add_argument(
        '-f',
        '--from',
        type=dateutil.parser.parse,
        help='new begin time',
    )
    edit_parser.add_argument(
        '-t',
        '--to',
        type=dateutil.parser.parse,
        help='new end time',
    )
    edit_parser.add_argument(
        '-c',
        '--count',
        type=int,
        help=f'new plan count (see {add_parser.prog} -h)',
    )

    command_action.add_parser(
        'list',
        description='show all plans in compact way',
    )

    delete_parser = command_action.add_parser(
        'delete',
        description='delete plan',
    )
    delete_parser.add_argument('id', type=int, help='plan id')

    show_parser = command_action.add_parser(
        'show',
        description='show specified plan',
    )
    show_parser.add_argument('id', type=int, help='plan id')

    command_action.add_parser(
        'check',
        help='check for plan triggerings and create tasks',
    )


def create_parser():
    parser = ArgumentParser(
        description='manage tasks, planned tasks and plans',
    )
    parser.add_argument('-u', '--user', help='current user')
    parser.add_argument('-c', '--config', help='path to config file')
    parser.add_argument('-s', '--storage', help='storage url')
    parser.add_argument('-l', '--logging', help='path to log directory')
    parser.add_argument('-ll', '--loglevel', help='logging level')
    parser.add_argument('-w', '--warnfilter', help='warnings filter')
    parser.add_argument(
        '-v',
        '--version',
        help='show version and exit',
        action='version',
        version=__import__('timelib').__version__,
    )

    subject_action = parser.add_subparsers(
        dest='subject',
        help='management subject',
    )
    subject_action.required = True

    configure_task_parser(subject_action)
    configure_planned_task_parser(subject_action)
    configure_plan_parser(subject_action)

    return parser
