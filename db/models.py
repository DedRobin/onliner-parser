from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)


class Products(Base):
    __tablename__ = "chat_ids"
    id = Column(Integer, primary_key=True)
    link = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relations
    user = relationship("User", back_populates="user")
