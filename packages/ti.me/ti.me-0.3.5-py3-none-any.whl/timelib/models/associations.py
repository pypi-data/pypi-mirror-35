from sqlalchemy import (
    Table,
    Column,
    Integer,
    ForeignKey,
)

from timelib.models.base import Base


task_blocking_task_association = Table(
    'task_blocking_task_associations',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('blocking_task_id', Integer, ForeignKey('tasks.id')),
)

task_target_task_association = Table(
    'task_target_task_associations',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('target_task_id', Integer, ForeignKey('tasks.id')),
)

planned_task_blocking_task_association = Table(
    'planned_task_blocking_task_associations',
    Base.metadata,
    Column('planned_task_id', Integer, ForeignKey('planned_tasks.id')),
    Column('blocking_task_id', Integer, ForeignKey('planned_tasks.id')),
)

planned_task_target_task_association = Table(
    'planned_tasks_target_tasks_associations',
    Base.metadata,
    Column('planned_task_id', Integer, ForeignKey('planned_tasks.id')),
    Column('target_task_id', Integer, ForeignKey('planned_tasks.id')),
)
