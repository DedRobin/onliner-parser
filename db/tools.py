import os
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db.models import Base

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_ECHO = bool(os.environ.get("DB_ECHO"))
DB_HOST = os.environ.get("DB_HOST", "localhost")


def _create_db_engine():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=DB_ECHO,
    )
    return engine


def _create_db_engine_if_not_exists(engine: Engine) -> None:
    if not database_exists(engine.url):
        create_database(engine.url)


def create_session() -> Session:
    engine = _create_db_engine()
    _create_db_engine_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    session = CurrentSession()
    return session
