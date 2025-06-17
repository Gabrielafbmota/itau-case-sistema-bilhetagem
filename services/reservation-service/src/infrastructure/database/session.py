from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from contextlib import contextmanager
from src.core.config import get_env_var

Base = declarative_base()


class DatabaseSession:

    def __init__(self) -> None:
        self.db_url, self.engine, self.SessionLocal = self.make_session()

    def make_session(self, *args, **kwargs):
        db_url = get_env_var("DATABASE_URL")
        engine = create_engine(db_url, echo=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return db_url, engine, SessionLocal

    def get_session(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @contextmanager
    def session_scope(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def close_engine(self):
        self.engine.dispose()
