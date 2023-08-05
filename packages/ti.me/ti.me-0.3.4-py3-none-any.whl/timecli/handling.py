from datetime import datetime

from dateutil.relativedelta import relativedelta

from timecli.logging import logged
from timecli.utils import gettext
from timecli.config import TIME_FORMAT
from timecli import views


@logged
def handle_task(manager, args, time_format=TIME_FORMAT):
    if args.command == 'add':
        with manager.save_after():
            task = manager.create_task(
                text=args.text or gettext(),
                from_time=vars(args)['from'] or datetime.now(),
                to_time=args.to,
                priority=args.priority.name if args.priority else 'normal',
                labels=args.labels or [],
                members=args.members or [],
                blocking_task_ids=args.blocking_tasks or [],
                target_task_ids=args.target_tasks or [],
            )

        print(f'Task successfully created:')
        print(views.task_compact(task, time_format))

    elif args.command == 'edit':
        with manager.save_after():
            task = manager.get_task(id=args.id)

            task.text = args.text or task.text
            task.from_time = vars(args)['from'] or task.from_time
            task.to_time = args.to or task.to_time
            task.priority = args.priority or task.priority
            task.completed = args.completed or task.completed
            task.archived = args.archived or task.archived
            if args.blocking_tasks is not None:
                task.blocking_tasks = [
                    manager.get_task(id=blocking_task_id)
                    for blocking_task_id
                    in args.blocking_tasks
                ]
            if args.target_tasks is not None:
                task.target_tasks = [
                    manager.get_task(id=target_task_id)
                    for target_task_id
                    in args.target_tasks
                ]
            if args.labels is not None:
                task.labels = args.labels
            if args.members is not None:
                task.members = list(
                    set(args.members + [manager.default_user]),
                )

        print(f'Task successfully edited:')
        print(views.task_compact(task, time_format))

    elif args.command == 'list':
        for task in manager.get_tasks(
            archived=args.archived,
            completed=args.completed,
            labels=args.labels or [],
        ):
            print(views.task_compact(task, time_format))

    elif args.command == 'delete':
        with manager.save_after():
            manager.delete_task(id=args.id)
        print(f'Task successfully deleted')

    elif args.command == 'show':
        task = manager.get_task(id=args.id)
        print(views.task_full(task, time_format))

    elif args.command == 'complete':
        with manager.save_after():
            manager.complete_task(id=args.id)
        print(f'Task successfully completed:')
        print(views.task_compact(manager.get_task(id=args.id), time_format))

    elif args.command == 'archive':
        with manager.save_after():
            manager.get_task(id=args.id).archived = True
        print(f'Task successfully archived:')
        print(views.task_compact(manager.get_task(id=args.id), time_format))

    elif args.command == 'block':
        with manager.save_after():
            blocking = manager.get_task(id=args.blocking)
            task = manager.get_task(id=args.id)
            task.blocking_tasks = list(
                set(task.blocking_tasks + [blocking])
            )
        print(f'Task:')
        print(views.task_compact(blocking, time_format))
        print(f'successfully blocked task:')
        print(views.task_compact(task, time_format))

    elif args.command == 'target':
        with manager.save_after():
            target = manager.get_task(id=args.target)
            task = manager.get_task(id=args.id)
            task.target_tasks = list(
                set(task.target_tasks + [target])
            )
        print(f'Task:')
        print(views.task_compact(task, time_format))
        print(f'successfully targeted at task:')
        print(views.task_compact(target, time_format))

    elif args.command == 'share':
        with manager.save_after():
            manager.share_task(id=args.id, members=args.members)
        print(f'Task successfully shared:')
        print(views.task_compact(manager.get_task(id=args.id), time_format))

    else:
        raise ValueError(f'Command {args.command} not found')


@logged
def handle_planned_task(manager, args, time_format=TIME_FORMAT):
    if args.command == 'add':
        with manager.save_after():
            planned_task = manager.create_planned_task(
                plan_id=args.plan,
                text=args.text or gettext(),
                from_time=vars(args)['from'] or relativedelta(),
                to_time=args.to,
                priority=args.priority.name if args.priority else 'normal',
                labels=args.labels or [],
                members=args.members or [],
                blocking_task_ids=args.blocking_tasks or [],
                target_task_ids=args.target_tasks or [],
            )

        print(f'Planned task successfully created')
        print(views.planned_task_compact(planned_task, time_format))

    elif args.command == 'edit':
        with manager.save_after():
            planned_task = manager.get_planned_task(id=args.id)

            planned_task.text = args.text or planned_task.text
            planned_task.from_time = (
                vars(args)['from']
                or planned_task.from_time
            )
            planned_task.to_time = args.to or planned_task.to_time
            planned_task.priority = args.priority or planned_task.priority
            planned_task.completed = args.completed or planned_task.completed
            planned_task.archived = args.archived or planned_task.archived
            if args.blocking_tasks is not None:
                planned_task.blocking_tasks = [
                    manager.get_planned_task(id=blocking_task_id)
                    for blocking_task_id
                    in args.blocking_tasks
                ]
            if args.target_tasks is not None:
                planned_task.target_tasks = [
                    manager.get_planned_task(id=target_task_id)
                    for target_task_id
                    in args.target_tasks
                ]
            if args.labels is not None:
                planned_task.labels = args.labels
            if args.members is not None:
                planned_task.members = list(
                    set(args.members + [manager.default_user]),
                )

        print(f'Planned task successfully edited:')
        print(views.planned_task_compact(planned_task, time_format))

    elif args.command == 'list':
        if args.plan:
            plan = manager.get_plan(id=args.plan)
        for planned_task in manager.get_planned_tasks(
            archived=args.archived,
            completed=args.completed,
            labels=args.labels or [],
        ):
            if args.plan is None or planned_task in plan:
                print(views.planned_task_compact(planned_task, time_format))

    elif args.command == 'delete':
        with manager.save_after():
            manager.delete_planned_task(id=args.id)
        print(f'Planned task successfully deleted')

    elif args.command == 'show':
        planned_task = manager.get_planned_task(id=args.id)

        print(views.planned_task_full(planned_task, time_format))

    else:
        raise ValueError(f'Command {args.command} not found')


@logged
def handle_plan(manager, args, time_format=TIME_FORMAT):
    if args.command == 'add':
        with manager.save_after():
            plan = manager.create_plan(
                delta=args.delta,
                from_time=vars(args)['from'] or datetime.now(),
                to_time=args.to,
                count=args.count,
            )

        print(f'Plan successfully created:')
        print(views.plan_compact(plan, time_format))

    elif args.command == 'edit':
        with manager.save_after():
            plan = manager.get_plan(id=args.id)

            plan.delta = args.delta or plan.delta
            plan.from_time = vars(args)['from'] or plan.from_time
            plan.to_time = args.to or plan.to_time
            plan.count = args.count or plan.count

        print(f'Plan successfully edited:')
        print(views.plan_compact(plan, time_format))

    elif args.command == 'list':
        for plan in manager.get_plans():
            print(views.plan_compact(plan, time_format))

    elif args.command == 'delete':
        with manager.save_after():
            manager.delete_plan(id=args.id)
        print(f'Plan successfully deleted')

    elif args.command == 'show':
        plan = manager.get_plan(id=args.id)

        print(views.plan_full(plan, time_format))

    elif args.command == 'check':
        with manager.save_after():
            for update in manager.get_updates():
                print(f'{update.time.strftime(time_format)}:')
                with manager.save_after():
                    tasks = manager.create_tasks_from_update(update)
                print(f'Tasks:')
                for task in tasks:
                    print(views.task_compact(task, time_format))
                print(f'successfully created')

    else:
        raise ValueError(f'Command {args.command} not found')


@logged
def root_handle(manager, args, time_format=TIME_FORMAT):
    if args.subject == 'task':
        handle_task(manager, args, time_format)
    elif args.subject == 'planned-task':
        handle_planned_task(manager, args, time_format)
    elif args.subject == 'plan':
        handle_plan(manager, args, time_format)
    else:
        raise ValueError(f'Subject {args.subject} not found')
