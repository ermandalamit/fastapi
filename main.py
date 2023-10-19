from typing import Union

from fastapi import FastAPI ,Depends,Request,status, HTTPException,Depends
app = FastAPI()
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from config.constants import API_ROOT_URI , MONGO_CONNECTION_URL
from modules.auth import login_for_access_token ,get_current_user
from modelClass.authModel import OAuthModel,TokenUserModel,GetUserModel
from pydantic import BaseModel
from config.databases import engine, SessionLocal
import dbModels.users
from dbModels.users import User
from sqlalchemy.orm import Session
from pymongo.mongo_client import MongoClient


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

dbModels.users.Base.metadata.create_all(bind=engine)
client = MongoClient(MONGO_CONNECTION_URL)
def get_connect_mysqldb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_connect_mongodb():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

mysqldb_dependency = Annotated[Session,Depends(get_connect_mysqldb)]
mongodb_dependency = Annotated[Session,Depends(get_connect_mongodb)]


@app.get("/")
async def read_root():
    return {"Hello": "World"}

#Oauth CREATE TOKEN API

@app.post(API_ROOT_URI+"/oauth")
async def authenticate_user(request: OAuthModel):
    return login_for_access_token(request)

@app.post(API_ROOT_URI+"/getUserByToken") #token check in header bearer
async def authenticate_user(token: Annotated[str, Depends(get_current_user)]):
    return {"message":"authorised user"}

# from dbModels.users import get_user_data

@app.post(API_ROOT_URI+"/getUserById",status_code=status.HTTP_200_OK)
async def getUserById(request: GetUserModel,db:mysqldb_dependency,token: Annotated[str, Depends(get_current_user)]):
    user = db.query(User).filter(User.id == request.user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user