# dependencies.py
from src.infrastructure.database.session import DatabaseSession


def get_db():
    db_gen = DatabaseSession().get_session()
    return next(db_gen)
