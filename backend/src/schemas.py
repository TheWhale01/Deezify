from pydantic import BaseModel

class UserBase(BaseModel):
    token: str
    service: int
    username: str

class UserCreate(BaseModel):
    pass

class User(BaseModel):
    id: int

    class Config:
        orm_mode = True
