import time
from datetime import datetime, timezone

from sqlalchemy.orm import Session
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.reservation_repository import ReservationRepository


def run_cleanup(interval_seconds=60):
    db_session = DatabaseSession().session_scope()
    with db_session as db:
        repository = ReservationRepository(db)
        print(f"[{datetime.now()}] 🕒 Iniciando scheduler de expiração de reservas...")

        while True:
            expired_reservations = repository.list_expired_unconfirmed()

            for reservation in expired_reservations:
                print(
                    f"[{datetime.now()}] ⛔ Cancelando reserva #{reservation.reservation_id}"
                )
                if reservation.reservation_id is None:
                    raise ValueError("Reservation ID cannot be None")
                repository.cancel(reservation.reservation_id)

            time.sleep(interval_seconds)
