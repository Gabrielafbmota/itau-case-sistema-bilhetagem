from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from src.infrastructure.database.session import Base


class TicketModel(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)  #
    event_id = Column(Integer, nullable=False, index=True)

    type = Column(String(50), nullable=True)  #

    price = Column(Numeric(10, 2), nullable=False)

    quantity_total = Column(Integer, nullable=False)
    quantity_available = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
