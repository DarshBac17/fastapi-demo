from pydantic import BaseModel


class AddressBase(BaseModel):
    address: str

class AddressOut(AddressBase):
    id: int

    class Config:
        from_attributes = True