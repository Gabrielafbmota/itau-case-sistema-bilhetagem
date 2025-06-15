from sqlalchemy import Column, Integer, String, DateTime, Text, func
from src.infrastructure.database.session import Base


class EventModel(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "bilheteria_schema"}

    event_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    location = Column(String(150), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
