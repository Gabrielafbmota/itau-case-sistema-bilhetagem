from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import get_env_var
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DatabaseSession:
    def make_session(self, *args, **kwargs):
        self.db_url = get_env_var("DATABASE_URL")
        self.engine = create_engine(self.db_url, echo=True)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def close_engine(self):
        self.engine.dispose()
