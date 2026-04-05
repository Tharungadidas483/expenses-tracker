from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class RecordCreate(BaseModel):
    amount: float
    category: str
    user_id: int


class RecordResponse(BaseModel):
    id: int
    amount: float
    category: str
    user_id: int

    class Config:
        from_attributes = True