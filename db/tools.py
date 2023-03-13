import os
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker, Session
from db.models import Base, Product, User

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_ECHO = os.environ.get("DB_ECHO") == "True"
DB_HOST = os.environ.get("DB_HOST", "localhost")


def create_session() -> Session:
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}", echo=DB_ECHO,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    session = CurrentSession()
    return session


async def write_link(username: str, session: Session, link: str) -> None:
    current_user = session.query(User).filter_by(username=username).all()[0]
    current_link = Product(link=link, tracking_frequency=30, user=current_user)
    session.add(current_link)
    session.commit()
