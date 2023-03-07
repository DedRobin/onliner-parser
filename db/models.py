from sqlalchemy import Integer, Float, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    link = Column(String)


class ChatID(Base):
    __tablename__ = "chat_ids"
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relations
    user = relationship("User", back_populates="user")
