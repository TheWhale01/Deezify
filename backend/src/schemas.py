from pydantic import BaseModel

class UserBase(BaseModel):
    token: str
    service: int
    username: str

class UserCreate(UserBase):
    pass

class User(UserCreate):
    id: int

    class Config:
        from_attributes = True
