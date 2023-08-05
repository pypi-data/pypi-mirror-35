from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Enum,
    String,
    Boolean,
    PickleType,
)
from sqlalchemy.orm import relationship

from timelib.models.base import Base
from timelib.models.task import TaskPriority
from timelib.models.associations import (
    planned_task_blocking_task_association,
    planned_task_target_task_association,
)


class PlannedTask(Base):
    __tablename__ = 'planned_tasks'

    id = Column(Integer, primary_key=True)
    completed = Column(Boolean, default=False)
    text = Column(String)
    from_time = Column(PickleType)
    to_time = Column(PickleType)
    archived = Column(Boolean)
    priority = Column(Enum(TaskPriority))
    labels = Column(PickleType)
    members = Column(PickleType)
    plan_id = Column(Integer, ForeignKey('plans.id'))

    plan = relationship('Plan', back_populates='planned_tasks')
    blocking_tasks = relationship(
        'PlannedTask',
        secondary=planned_task_blocking_task_association,
        primaryjoin=(
            id == planned_task_blocking_task_association.c.planned_task_id
        ),
        secondaryjoin=(
            id == planned_task_blocking_task_association.c.blocking_task_id
        ),
    )
    target_tasks = relationship(
        'PlannedTask',
        secondary=planned_task_target_task_association,
        primaryjoin=(
            id == planned_task_target_task_association.c.planned_task_id
        ),
        secondaryjoin=(
            id == planned_task_target_task_association.c.target_task_id
        ),
    )
