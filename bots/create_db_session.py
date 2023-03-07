from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db.models import Base
from db.utils import create_db_engine, create_db_engine_if_not_exists


def create_session() -> Session:
    engine = create_db_engine()
    create_db_engine_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
    return current_session
