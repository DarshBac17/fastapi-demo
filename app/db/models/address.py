from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, index=True)
    city = Column(String,nullable=True)
    pincode = Column(Integer, nullable=True)
    # country = Column(String,nullable=True)


    # user_id = Column(Integer, ForeignKey("users.id"))
    #
    # user = relationship("User", back_populates="addresses")
