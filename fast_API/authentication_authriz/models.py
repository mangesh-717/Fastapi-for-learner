from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class Profile(BaseModel):
    username: str
    email: str
