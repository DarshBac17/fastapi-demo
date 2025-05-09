from typing import Union

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.address import *
from app.db.models.address import *

def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Address).offset(skip).limit(limit).all()

async def create_address(db: Union[AsyncSession, Session], address: AddressBase):
    db_address = Address(**address.dict())
    db.add(db_address)

    if isinstance(db, AsyncSession):
        await db.commit()
        await db.refresh(db_address)
    else:
        db.commit()
        db.refresh(db_address)

    return db_address

def update_address(db: Session, address_id: int, address: AddressBase):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        db_address.address = address.address
        db.commit()
        db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address
