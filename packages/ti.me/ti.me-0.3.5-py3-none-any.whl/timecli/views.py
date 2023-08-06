from termcolor import colored

from timelib.models import TaskPriority
from timecli.logging import logged
from timecli.config import TIME_FORMAT
from timecli.utils import stringify_relativedelta


@logged
def task_compact(task, time_format=TIME_FORMAT):
    id = f'#{task.id}'
    if task.completed:
        id = colored(id, 'green')
    text = task.text.replace('\r', ' ').replace('\n', ' ')
    text = f'{text[:20]}{text[20:] and "..."}'
    if task.priority == TaskPriority.CRITICAL:
        text = colored(text, 'red')
    elif task.priority == TaskPriority.IMPORTANT:
        text = colored(text, 'yellow')
    elif task.priority == TaskPriority.LOW:
        text = colored(text, 'grey')
    if task.archived:
        text = f'{colored("(arch)", "white", "on_red")} {text}'
    labels = ' '.join(
        colored(label, on_color='on_grey')
        for label
        in task.labels[:3]
    )
    if len(task.labels) > 3:
        labels += f' and {len(task.labels) - 3} other'
    item = f'{id} {text} {labels}'

    return item


@logged
def task_full(task, time_format=TIME_FORMAT):
    view = []
    view.append(f'#{task.id}')
    if task.archived:
        view.append(colored("(archived)", "white", "on_red"))
    if task.to_time:
        view.append(
            f'{task.from_time.strftime(time_format)}'
            f' - {task.to_time.strftime(time_format)}',
        )
    else:
        view.append(task.from_time.strftime(time_format))
    view.append(f'created: {task.created_at.strftime(time_format)}')
    view.append(f'updated: {task.updated_at.strftime(time_format)}')
    view.append(' '.join(
        colored(label, on_color='on_grey')
        for label
        in task.labels
    ))
    if task.priority == TaskPriority.CRITICAL:
        view.append(colored(f'priority: {task.priority.name}', 'red'))
    elif task.priority == TaskPriority.IMPORTANT:
        view.append(colored(f'priority: {task.priority.name}', 'yellow'))
    elif task.priority == TaskPriority.NORMAL:
        view.append(task.priority.name)
    elif task.priority == TaskPriority.LOW:
        view.append(colored(f'priority: {task.priority.name}', 'grey'))
    view.append(f'members: {", ".join(member for member in task.members)}')
    if task.blocking_tasks:
        view.append('blocked by:')
        for blocking_task in task.blocking_tasks:
            view.append(task_compact(blocking_task, time_format))
    if task.target_tasks:
        view.append('triggers:')
        for target_task in task.target_tasks:
            view.append(task_compact(target_task, time_format))
    view.append(task.text)

    return '\n'.join(view)


@logged
def planned_task_compact(planned_task, time_format=TIME_FORMAT):
    text = planned_task.text.replace('\r', ' ').replace('\n', ' ')
    text = f'{text[:20]}{text[20:] and "..."}'
    if planned_task.priority == TaskPriority.CRITICAL:
        text = colored(text, 'red')
    elif planned_task.priority == TaskPriority.IMPORTANT:
        text = colored(text, 'yellow')
    elif planned_task.priority == TaskPriority.LOW:
        text = colored(text, 'grey')
    labels = ' '.join(
        colored(label, on_color='on_grey')
        for label
        in planned_task.labels[:3]
    )
    if len(planned_task.labels) > 3:
        labels += f' and {len(planned_task.labels) - 3} other'
    item = f'#{planned_task.id} (plan: {planned_task.plan_id}) {text} {labels}'

    return item


@logged
def planned_task_full(planned_task, time_format=TIME_FORMAT):
    view = []
    view.append(f'#{planned_task.id}')
    view.append('plan:')
    view.append(plan_compact(planned_task.plan, time_format))
    if planned_task.archived:
        view.append(colored("(archived)", "white", "on_red"))
    if planned_task.to_time:
        view.append(
            f'{stringify_relativedelta(planned_task.from_time)}'
            f' - {stringify_relativedelta(planned_task.to_time)}',
        )
    else:
        view.append(stringify_relativedelta(planned_task.from_time))
    view.append(' '.join(
        colored(label, on_color='on_grey')
        for label
        in planned_task.labels
    ))
    if planned_task.priority == TaskPriority.CRITICAL:
        view.append(colored(f'priority: {planned_task.priority.name}', 'red'))
    elif planned_task.priority == TaskPriority.IMPORTANT:
        view.append(
            colored(f'priority: {planned_task.priority.name}', 'yellow'),
        )
    elif planned_task.priority == TaskPriority.NORMAL:
        view.append(planned_task.priority.name)
    elif planned_task.priority == TaskPriority.LOW:
        view.append(colored(f'priority: {planned_task.priority.name}', 'grey'))
    view.append(
        f'members: {", ".join(member for member in planned_task.members)}',
    )
    if planned_task.blocking_tasks:
        view.append('blocked by:')
        for blocking_task in planned_task.blocking_tasks:
            view.append(planned_task_compact(blocking_task, time_format))
    if planned_task.target_tasks:
        view.append('triggers:')
        for target_task in planned_task.target_tasks:
            view.append(planned_task_compact(target_task, time_format))
    view.append(planned_task.text)

    return '\n'.join(view)


@logged
def plan_compact(plan, time_format=TIME_FORMAT):
    item = f'#{plan.id} (delta: {stringify_relativedelta(plan.delta)})'
    if plan.planned_tasks:
        planned_tasks = ', '.join(
            str(planned_task.id)
            for planned_task
            in plan.planned_tasks[:5]
        )
        if len(plan.planned_tasks) > 5:
            planned_tasks += f' and {len(plan.planned_tasks) - 5} other'
        item += ' (planned tasks: {planned_tasks})'

    return item


@logged
def plan_full(plan, time_format=TIME_FORMAT):
    view = []
    view.append(f'#{plan.id}')
    view.append(f'delta: {stringify_relativedelta(plan.delta)}')
    if plan.to_time:
        view.append(
            f'{plan.from_time.strftime(time_format)}'
            f' - {plan.to_time.strftime(time_format)}',
        )
    else:
        view.append(plan.from_time.strftime(time_format))
    view.append(f'last time: {plan.last_time.strftime(time_format)}')
    if plan.count:
        view.append(f'count: {plan.count}')
        view.append(f'last count: {plan.last_count}')
    view.append(f'member: {plan.member}')
    if plan.planned_tasks:
        view.append('planned tasks:')
        for planned_task in plan.planned_tasks:
            view.append(planned_task_compact(planned_task, time_format))

    return '\n'.join(view)
