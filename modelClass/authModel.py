from pydantic import BaseModel

class OAuthModel(BaseModel):
    username: str
    name: str | None = None
    email: str | None = None
    password: str | None = None
    disabled:bool 

class TokenUserModel(BaseModel):
    token: str

class GetUserModel(BaseModel):
    user_id:int