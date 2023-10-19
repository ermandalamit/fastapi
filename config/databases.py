from sqlalchemy import  create_engine
from sqlalchemy.connectors import Connector
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pymongo.mongo_client import MongoClient


URL_DATABSE = "mysql+pymysql://root:rootpassword@localhost:3306/wishfin"

engine = create_engine(URL_DATABSE)

SessionLocal = sessionmaker(autoflush=False,autocommit= False,bind=engine)

Base = declarative_base()



