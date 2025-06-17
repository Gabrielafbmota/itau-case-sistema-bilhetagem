from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from src.infrastructure.database.session import Base


class ReservationModel(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    ticket_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    reserved_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    is_confirmed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Reservation(reservation_id={self.reservation_id}, user_id={self.user_id}, ticket_id={self.ticket_id})>"
