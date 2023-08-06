from enum import IntEnum
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Boolean,
    PickleType,
    Enum,
)
from sqlalchemy.orm import relationship

from timelib.models.base import Base
from timelib.models.associations import (
    task_blocking_task_association,
    task_target_task_association,
)


class TaskPriority(IntEnum):
    CRITICAL = 1
    IMPORTANT = 2
    NORMAL = 3
    LOW = 4


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    completed = Column(Boolean, default=False)
    text = Column(String)
    from_time = Column(DateTime)
    to_time = Column(DateTime)
    archived = Column(Boolean)
    priority = Column(Enum(TaskPriority))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
    )
    labels = Column(PickleType)
    members = Column(PickleType)
    blocking_tasks = relationship(
        'Task',
        secondary=task_blocking_task_association,
        primaryjoin=id == task_blocking_task_association.c.task_id,
        secondaryjoin=id == task_blocking_task_association.c.blocking_task_id,
    )
    target_tasks = relationship(
        'Task',
        secondary=task_target_task_association,
        primaryjoin=id == task_target_task_association.c.task_id,
        secondaryjoin=id == task_target_task_association.c.target_task_id,
    )
