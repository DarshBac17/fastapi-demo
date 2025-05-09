import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.schemas.address import AddressBase, AddressOut
from app.services import adress_services
from app.db.session import get_db, get_async_session

router = APIRouter(prefix="/address", tags=["Address"])



@router.post("/addresses-async/", response_model=AddressOut)
async def create_address_async(address: AddressBase, db: AsyncSession = Depends(get_async_session)):
    await asyncio.sleep(20)
    return await adress_services.create_address(db=db, address=address)

@router.post("/addresses-sync/", response_model=AddressOut)
async def create_address(address: AddressBase, db: Session = Depends(get_db)):
    return adress_services.create_address(db=db, address=address)







@router.get("/addresses/", response_model=list[AddressOut])
def read_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return adress_services.get_addresses(db, skip=skip, limit=limit)

@router.get("/addresses/{address_id}", response_model=AddressOut)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = adress_services.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.put("/addresses/{address_id}", response_model=AddressOut)
def update_address(address_id: int, address: AddressBase, db: Session = Depends(get_db)):
    db_address = adress_services.update_address(db, address_id, address)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.delete("/addresses/{address_id}", response_model=AddressOut)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = adress_services.delete_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
