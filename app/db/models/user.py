from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer,nullable=True)
    hobby = Column(String,nullable=True)
    phone = Column(String,nullable=True)

    city = Column(String,nullable=True)

    # # Optional: Relationship back to posts
    # addresses = relationship("Address", back_populates="user")