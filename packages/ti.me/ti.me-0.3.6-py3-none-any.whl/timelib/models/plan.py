from sqlalchemy import (
    Integer,
    Column,
    DateTime,
    PickleType,
    String,
)
from sqlalchemy.orm import relationship

from timelib.models.base import Base


class Plan(Base):
    __tablename__ = 'plans'

    id = Column(Integer, primary_key=True)
    from_time = Column(DateTime)
    to_time = Column(DateTime)
    last_time = Column(DateTime)
    delta = Column(PickleType)
    count = Column(Integer)
    last_count = Column(Integer, default=0)
    member = Column(String)

    planned_tasks = relationship('PlannedTask', back_populates='plan')
