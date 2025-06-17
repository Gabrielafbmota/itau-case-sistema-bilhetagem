from apscheduler.schedulers.background import BackgroundScheduler
from src.infrastructure.database.session import DatabaseSession
from src.infrastructure.repositories.reservation_repository import ReservationRepository
from src.application.clients.ticket_client import TicketClient  # novo client HTTP
import logging

logger = logging.getLogger("scheduler")


def cleanup_expired():
    db = next(DatabaseSession().get_session())
    reservation_repo = ReservationRepository(db)
    ticket_client = TicketClient()

    expired = reservation_repo.list_expired_unconfirmed()
    logger.info(f"Expiring {len(expired)} reservations")

    for res in expired:
        try:
            ticket_client.increment_ticket_quantity(res.ticket_id, res.quantity)
            if res.reservation_id:
                reservation_repo.cancel(res.reservation_id)
        except Exception as e:
            logger.error(f"Erro ao processar reserva {res.reservation_id}: {e}")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(cleanup_expired, "interval", minutes=5)
    scheduler.start()
