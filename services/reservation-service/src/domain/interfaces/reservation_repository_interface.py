from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.reservation_entity import Reservation


class IReservationRepository(ABC):

    @abstractmethod
    def create(self, reservation: Reservation) -> Reservation:
        pass

    @abstractmethod
    def get_by_id(self, reservation_id: int) -> Optional[Reservation]:
        pass

    @abstractmethod
    def list_by_user(self, user_id: int) -> List[Reservation]:
        pass

    @abstractmethod
    def list_expired_unconfirmed(self) -> List[Reservation]:
        pass

    @abstractmethod
    def confirm(self, reservation_id: int) -> None:
        pass

    @abstractmethod
    def cancel(self, reservation_id: int) -> None:
        pass
