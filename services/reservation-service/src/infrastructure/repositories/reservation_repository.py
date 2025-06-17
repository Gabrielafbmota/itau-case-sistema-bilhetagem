from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.entities.reservation_entity import Reservation
from src.domain.interfaces.reservation_repository_interface import (
    IReservationRepository,
)
from src.infrastructure.database.models.reservation_model import ReservationModel


class ReservationRepository(IReservationRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, reservation: Reservation) -> Reservation:
        db_model = ReservationModel(**reservation.dict(exclude={"reservation_id"}))
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return Reservation.from_orm(db_model)

    def get_by_id(self, reservation_id: int) -> Optional[Reservation]:
        model = (
            self.db.query(ReservationModel)
            .filter_by(reservation_id=reservation_id)
            .first()
        )
        return Reservation.from_orm(model) if model else None

    def list_by_user(self, user_id: int) -> List[Reservation]:
        models = self.db.query(ReservationModel).filter_by(user_id=user_id).all()
        return [Reservation.from_orm(m) for m in models]

    def list_expired_unconfirmed(self) -> List[Reservation]:
        current_time = datetime.utcnow()
        models = (
            self.db.query(ReservationModel)
            .filter(
                ReservationModel.expires_at < current_time,
                ReservationModel.is_confirmed.is_(False),
            )
            .all()
        )
        return [Reservation.from_orm(m) for m in models]

    def confirm(self, reservation_id: int) -> None:
        self.db.query(ReservationModel).filter_by(reservation_id=reservation_id).update(
            {"is_confirmed": True}
        )
        self.db.commit()

    def cancel(self, reservation_id: int) -> None:
        try:
            result = (
                self.db.query(ReservationModel)
                .filter_by(reservation_id=reservation_id)
                .delete()
            )

            if result == 0:
                print(f"[WARN] Nenhuma reserva encontrada com ID {reservation_id}")
            else:
                print(f"[INFO] Reserva {reservation_id} cancelada com sucesso.")

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(f"[ERROR] Erro ao cancelar reserva {reservation_id}: {e}")
            raise
