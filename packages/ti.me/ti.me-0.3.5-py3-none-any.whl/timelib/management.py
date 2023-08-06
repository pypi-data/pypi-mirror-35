import warnings
from contextlib import contextmanager
from datetime import datetime
from collections import namedtuple

from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from timelib.models import (
    Base,
    Task,
    TaskPriority,
    Plan,
    PlannedTask,
)
from timelib.exceptions import (
    NotFoundError,
    InvalidActionError,
    StorageError,
    DifferentPlanError,
    ActionAlreadyPerformedWarning,
    ForeignRelatedTaskWarning,
)
from timelib.logging import (
    logged,
    get_logger,
)


__all__ = ['create_session', 'Manager']


@logged
def create_session(database_url):
    """Creates database session instance suitable for Manager.

    Args:
        database_url: SQLAlchemy compatible url with database info.

    Returns:
        Database session instance suitable for Manager.

    Raises:
        StorageError: Raised from internal storage exceptions.

    Examples:

        >>> create_session('sqlite://')  # doctest: +ELLIPSIS
        <sqlalchemy.orm.session.Session object at 0x...>

    """
    try:
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)()
    except Exception as e:
        raise StorageError from e


Update = namedtuple('Update', ['time', 'tasks'])


class Manager:
    """API class for interaction with library models.

    Attributes:
        session: Database session instance.
        default_user: Default user for all operations.

    Examples:

        >>> session = create_session('sqlite://')
        >>> Manager(session, 'stranger')  # doctest: +ELLIPSIS
        <management.Manager object at 0x...>

    """

    @logged
    def __init__(
        self,
        session,
        default_user,
    ):
        super().__init__()

        self.session = session
        self.default_user = default_user

    @logged
    def reset_storage(self):
        """Removes all data from storage."""
        try:
            Base.metadata.drop_all(self.session.bind)
            Base.metadata.create_all(self.session.bind)
        except Exception as e:
            raise StorageError from e

    @logged
    def save(self):
        """Saves all changes."""
        self.session.commit()

    @logged
    def cancel(self):
        """Cancels all changes."""
        self.session.rollback()

    @contextmanager
    @logged
    def save_after(self):
        """Saves changes after several operations.

        Examples:

            >>> manager = Manager(create_session('sqlite://'), 'stranger')
            >>> with manager.save_after():
            ...     manager.create_task()  # doctest: +ELLIPSIS
            <timelib.models.task.Task object at 0x...>

        Raises:
            Any exception from with block.
        """
        try:
            yield self
            self.save()
            get_logger().info('Save')
        except Exception:
            self.cancel()
            get_logger().info('Cancel')
            raise

    @logged
    def delete_task(self, id, user=None):
        """Deletes task from storage.

        Raises:
            InvalidActionError: Raised when other tasks refer to currently
                deleted task.
        """
        user = user or self.default_user

        if (
            len(self.get_tasks(user=user, blocking_task_ids=[id]))
            or len(self.get_tasks(user=user, target_task_ids=[id]))
        ):
            raise InvalidActionError(
                f'Other tasks refer to task with id={id!r}, user={user!r}',
            )

        self.session.delete(self.get_task(id=id, user=user))

    @logged
    def get_task(self, id, user=None):
        """Returns task by id.

        Raises:
            NotFoundError: Raised when requested task doesn't exist.
        """
        user = user or self.default_user

        try:
            return next(
                task
                for task
                in self.session.query(Task).all()
                if task.id == id and user in task.members
            )
        except StopIteration as e:
            raise NotFoundError(
                f'Task with id={id!r}, user={user!r} not found',
            ) from e

    @logged
    def get_tasks(
        self,
        user=None,
        text=None,
        from_time=None,
        to_time=None,
        priority=None,
        completed=None,
        archived=None,
        members=[],
        labels=[],
        blocking_task_ids=[],
        target_task_ids=[],
    ):
        """Returns tasks filtered by set of keys and sorded by priority.

        Args:
            See Manager.create_task.
            text: Part of task text.
            from_time: Begin of required period.
            to_time: End of required period.
            members: Incomplete list of task members.
            labels: Task label branches.
            blocking_task_ids: Incomplete list of blocking tasks.
            target_task_ids: Incomplete list of target tasks.
        """
        user = user or self.default_user

        return sorted(
            [
                task
                for task
                in self.session.query(Task).all()
                if (
                    ((user is None) or user in task.members)
                    and (
                        (not members)
                        or all(member in task.members for member in members)
                    )
                    and (text is None or text in task.text)
                    and ((from_time is None) or from_time < task.from_time)
                    and (
                        (to_time is None)
                        or ((task.to_time or task.from_time) < to_time)
                    )
                    and ((priority is None) or task.priority == priority)
                    and ((completed is None) or task.completed == completed)
                    and ((archived is None) or task.archived == archived)
                    and (
                        (not labels)
                        or all(
                            any(
                                (
                                    task_label == label
                                    or task_label.startswith(f'{label}.')
                                )
                                for task_label
                                in task.labels
                            )
                            for label
                            in labels
                        )
                    )
                    and (
                        (not blocking_task_ids)
                        or all(
                            self.get_task(
                                id=blocking_task_id,
                                user=user,
                            ) in task.blocking_tasks
                            for blocking_task_id
                            in blocking_task_ids
                        )
                    )
                    and (
                        (not target_task_ids)
                        or all(
                            self.get_task(
                                id=target_task_id,
                                user=user,
                            ) in task.target_tasks
                            for target_task_id
                            in target_task_ids
                        )
                    )
                )
            ],
            key=lambda task: task.priority,
        )

    @logged
    def create_task(
        self,
        user=None,
        text='',
        from_time=None,
        to_time=None,
        labels=[],
        priority='normal',
        completed=False,
        archived=False,
        members=[],
        blocking_task_ids=[],
        target_task_ids=[],
    ):
        """Creates task with given parameters.

        Args:
            user: Task member.
            text: Task description.
            from_time: Begin of period when task is performed.
            to_time: End of period when task is performed.
            priority: Task priority.
            completed: Is task completed.
            archived: Is task archived.
            members: Task members.
            labels: Task labels.
            blocking_task_ids: Blocking tasks.
            target_task_ids: Target tasks.

        Raises:
            NotFoundError: Raised when given priority is invalid.
            ActionAlreadyPerformedWarning: Raised when user in given members.
        """
        user = user or self.default_user
        if not from_time:
            from_time = datetime.now()
            get_logger().info(
                'Use datetime.now() for not provided from_time',
            )
        try:
            priority = TaskPriority[priority.upper()]
        except KeyError:
            raise NotFoundError(f'Task priority {priority!r} does not exist')
        blocking_tasks = [
            self.get_task(blocking_task_id, user=user)
            for blocking_task_id
            in blocking_task_ids
        ]
        target_tasks = [
            self.get_task(target_task_id, user=user)
            for target_task_id
            in target_task_ids
        ]

        if user in members:
            warnings.warn(
                'User already in members',
                ActionAlreadyPerformedWarning,
            )

        task = Task(
            members=list(set([user] + members)),
            text=text,
            from_time=from_time,
            to_time=to_time,
            labels=labels,
            priority=priority,
            completed=completed,
            archived=archived,
            blocking_tasks=blocking_tasks,
            target_tasks=target_tasks,
        )
        self.session.add(task)
        return task

    @logged
    def share_task(
        self,
        id,
        members,
        user=None
    ):
        """Shares task with other users

        Raises:
            ActionAlreadyPerformedWarning: Raises when some users are already
                members.
        """
        user = user or self.default_user
        task = self.get_task(id=id, user=user)

        if any(member in task.members for member in members):
            warnings.warn(
                'Some members already in task\'s members',
                ActionAlreadyPerformedWarning,
            )

        task.members = list(set(task.members + members))

    @logged
    def complete_task(
        self,
        id,
        user=None
    ):
        """Completes task

        Raises:
            ActionAlreadyPerformedWarning: Raised when task is already
                completed.
        """
        user = user or self.default_user
        task = self.get_task(id=id, user=user)

        if all(
            task.completed
            for task
            in task.blocking_tasks
            if user in task.members
        ):
            if task.completed:
                warnings.warn(
                    'Task already completed',
                    ActionAlreadyPerformedWarning,
                )
            task.completed = True
            for target_task in task.target_tasks:
                if user in target_task.members:
                    self.complete_task(id=target_task.id, user=user)
                else:
                    warnings.warn(
                        'User is not member of target task',
                        ForeignRelatedTaskWarning,
                    )
        else:
            raise InvalidActionError('Task has uncompleted blocking tasks')

    @logged
    def delete_planned_task(self, id, user=None):
        """Deletes planned task from storage.

        Raises:
            InvalidActionError: Raised when other tasks refer to currently
                deleted task.
        """
        user = user or self.default_user

        if (
            self.get_planned_tasks(user=user, blocking_task_ids=[id])
            or self.get_planned_tasks(user=user, target_task_ids=[id])
        ):
            raise InvalidActionError(
                f'Other planned tasks refer to planned task with'
                f' id={id!r}, user={user!r}',
            )

        planned_task = self.get_planned_task(id=id, user=user)
        planned_task.plan.planned_tasks.remove(planned_task)
        self.session.delete(planned_task)

    @logged
    def get_planned_task(self, id, user=None):
        """Returns planned task by id.

        Raises:
            NotFoundError: Raised when requested task doesn't exist.
        """
        user = user or self.default_user

        try:
            return next(
                planned_task
                for planned_task
                in self.session.query(PlannedTask).all()
                if planned_task.id == id and planned_task.plan.member == user
            )
        except StopIteration as e:
            raise NotFoundError(
                f'Planned task with id={id!r}, user={user!r} not found',
            ) from e

    @logged
    def get_planned_tasks(
        self,
        user=None,
        text=None,
        from_time=None,
        to_time=None,
        priority=None,
        completed=None,
        archived=None,
        plan_id=None,
        labels=[],
        members=[],
        blocking_task_ids=[],
        target_task_ids=[],
    ):
        """Returns planned tasks filtered by set of keys.

        Args:
            See Manager.get_tasks.
            from_time: Begin of required period related to creation time.
            to_time: End of required period related to creation time.
            plan_id: Plan that contains planned task.
        """
        user = user or self.default_user

        return [
            planned_task
            for planned_task
            in self.session.query(PlannedTask).all()
            if (
                ((user is None) or planned_task.plan.member == user)
                and ((plan_id is None) or planned_task.plan_id == plan_id)
                and (
                    (not members)
                    or all(
                        member in planned_task.members
                        for member
                        in members
                    )
                )
                and (text is None or text in planned_task.text)
                and ((from_time is None) or from_time < planned_task.from_time)
                and (
                    (to_time is None)
                    or (
                        (
                            planned_task.to_time or planned_task.from_time
                        ) < to_time
                    )
                )
                and ((priority is None) or planned_task.priority == priority)
                and (
                    (completed is None)
                    or planned_task.completed == completed
                )
                and ((archived is None) or planned_task.archived == archived)
                and (
                    (not labels)
                    or all(
                        any(
                            (
                                task_label == label
                                or task_label.startswith(f'{label}.')
                            )
                            for task_label
                            in planned_task.labels
                        )
                        for label
                        in labels
                    )
                )
                and (
                    (not blocking_task_ids)
                    or all(
                        self.get_planned_task(
                            id=blocking_task_id,
                            user=user,
                        ) in planned_task.blocking_tasks
                        for blocking_task_id
                        in blocking_task_ids
                    )
                )
                and (
                    (not target_task_ids)
                    or all(
                        self.get_planned_task(
                            id=target_task_id,
                            user=user,
                        ) in planned_task.target_tasks
                        for target_task_id
                        in target_task_ids
                    )
                )
            )
        ]

    @logged
    def create_planned_task(
        self,
        plan_id,
        user=None,
        text='',
        from_time=None,
        to_time=None,
        labels=[],
        priority='normal',
        completed=False,
        archived=False,
        members=[],
        blocking_task_ids=[],
        target_task_ids=[],
    ):
        """Creates planned task with given parameters.

        Args:
            See Manager.create_task.
            from_time: Begin of period when task is performed related to
                creation time.
            to_time: End of period when task is performed related to creation
                time.
            plan_id: Plan that will contain planned task.

        Raises:
            See Manager.create_task.
            DifferentPlanError: Raised when related tasks are in other plan.
        """
        user = user or self.default_user
        if not from_time:
            from_time = relativedelta()
            get_logger().info(
                'Use relativedelta() for not provided from_time',
            )
        try:
            priority = TaskPriority[priority.upper()]
        except KeyError:
            raise NotFoundError(f'Task priority {priority!r} does not exist')
        blocking_tasks = [
            self.get_planned_task(blocking_task_id, user=user)
            for blocking_task_id
            in blocking_task_ids
        ]
        if any(
            blocking_task.plan_id != plan_id
            for blocking_task
            in blocking_tasks
        ):
            raise DifferentPlanError(
                'One of blocking tasks is in different plan',
            )
        target_tasks = [
            self.get_planned_task(target_task_id, user=user)
            for target_task_id
            in target_task_ids
        ]
        if any(target_task.plan_id != plan_id for target_task in target_tasks):
            raise DifferentPlanError(
                'One of target tasks is in different plan',
            )

        if user in members:
            warnings.warn(
                'User already in members',
                ActionAlreadyPerformedWarning,
            )

        planned_task = PlannedTask(
            plan_id=plan_id,
            members=list(set([user] + members)),
            text=text,
            from_time=from_time,
            to_time=to_time,
            labels=labels,
            priority=priority,
            completed=completed,
            archived=archived,
            blocking_tasks=blocking_tasks,
            target_tasks=target_tasks,
        )
        self.session.add(planned_task)
        return planned_task

    @logged
    def delete_plan(self, id, user=None):
        """Deletes plan with its planned tasks from storage."""
        user = user or self.default_user

        plan = self.get_plan(id=id, user=user)
        get_logger().info(
            f'Delete {len(plan.planned_tasks)} planned tasks',
        )
        for planned_task in plan.planned_tasks:
            self.session.delete(planned_task)
        self.session.delete(plan)

    @logged
    def get_plan(self, id, user=None):
        """Returns plan by id.

        Raises:
            NotFoundError: Raised when requested plan doesn't exist.
        """
        user = user or self.default_user

        try:
            return next(
                plan
                for plan
                in self.session.query(Plan).all()
                if plan.id == id and plan.member == user
            )
        except StopIteration as e:
            raise NotFoundError(
                f'Plan with id={id!r}, user={user!r} not found',
            ) from e

    @logged
    def get_plans(
        self,
        user=None,
        from_time=None,
        to_time=None,
        last_time=None,
        delta=None,
        count=None,
        last_count=None,
        planned_task_ids=[],
    ):
        """Returns plans filtered by set of keys.

        Args:
            See Manager.create_plan.
            from_time: Begin of required period.
            to_time: End of required period.
            last_time: Last time plan triggered.
            last_count: Number of plan triggerings.
            planned_task_ids: Incomplete list of planned tasks.
        """
        user = user or self.default_user

        return [
            plan
            for plan
            in self.session.query(Plan).all()
            if (
                plan.member == user
                and (
                    (not planned_task_ids)
                    or all(
                        self.get_planned_task(
                            id=planned_task_id,
                            user=user,
                        ) in plan.planned_tasks
                        for planned_task_id
                        in planned_task_ids
                    )
                )
                and ((from_time is None) or from_time < plan.from_time)
                and (
                    (to_time is None)
                    or ((plan.to_time or plan.from_time) < to_time)
                )
                and ((last_time is None) or plan.last_time == last_time)
                and ((delta is None) or plan.delta == delta)
                and ((count is None) or plan.count == count)
                and ((last_count is None) or plan.last_count == last_count)
            )
        ]

    @logged
    def create_plan(
        self,
        delta,
        user=None,
        from_time=None,
        to_time=None,
        count=None,
    ):
        """Creates plan with given parameters.

        Args:
            user: Plan owner.
            delta: Relative time delta between plan triggerings.
            from_time: Begin of period when plan is performed.
            to_time: End of period when task is performed.
            count: Number of plan triggerings.
        """
        user = user or self.default_user
        if not from_time:
            from_time = datetime.now()
            get_logger().info(
                'Use datetime.now() for not provided from_time',
            )

        plan = Plan(
            member=user,
            from_time=from_time,
            last_time=from_time,
            to_time=to_time,
            delta=delta,
            count=count,
        )
        self.session.add(plan)
        return plan

    @logged
    def get_updates(
        self,
        user=None,
    ):
        """Returns updates for all plans in period from last times to now.

        Yields:
            Next update with triggering time and tasks that have been planned.
        """
        user = user or self.default_user

        for plan in self.get_plans(user=user):
            while (
                ((plan.count is None) or plan.last_count < plan.count)
                and ((plan.to_time is None) or plan.last_time < plan.to_time)
                and plan.last_time < datetime.now()
            ):
                get_logger().info(
                    f'Yield {len(plan.planned_tasks)} tasks'
                    f' at {plan.last_time}',
                )
                yield Update(time=plan.last_time, tasks=plan.planned_tasks)
                plan.last_time += plan.delta
                plan.last_count += 1

    @logged
    def create_tasks_from_update(
        self,
        update,
        user=None,
    ):
        """Creates tasks from planneedd tasks with update time."""
        user = user or self.default_user

        tasks = {}
        for planned_task in update.tasks:
            tasks[planned_task.id] = self.create_task(
                members=planned_task.members,
                text=planned_task.text,
                completed=planned_task.completed,
                from_time=update.time + planned_task.from_time,
                to_time=(
                    planned_task.to_time
                    and update.time + planned_task.to_time
                ),
                archived=planned_task.archived,
                priority=planned_task.priority.name,
                labels=planned_task.labels,
            )
        for planned_task in update.tasks:
            tasks[planned_task.id].blocking_tasks = [
                tasks[blocking_task.id]
                for blocking_task
                in planned_task.blocking_tasks
            ]
            tasks[planned_task.id].target_tasks = [
                tasks[target_task.id]
                for target_task
                in planned_task.target_tasks
            ]
        self.save()
        get_logger().info(f'Create {len(tasks)} tasks')

        return tasks.values()
