from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True




def main():

    user = UserOut(
        id=1,
        name="John Doe",
        email="d@gmail.com"
    )

    user.id = "test"

    print("Hello, World!", user)

if __name__ == "__main__":
    main()