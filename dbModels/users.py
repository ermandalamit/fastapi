from sqlalchemy import Boolean , Column , Integer , String , String, ForeignKey
from config.databases import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
class User(Base):
    __tablename__ = 'xkyknzl5dwfyk4hg_master_user'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]= mapped_column(String(30))
    full_name: Mapped[str] = mapped_column(String(30))








# rom config.databases import conn
# class User(conn):
#     __tablename__ = "Users"   

#     def get_user_data(userId):
#         cursor = conn.cursor()
#         query = "SELECT * FROM users WHERE id=5"
#         cursor.execute(query)
#         conn.commit()        
#         cursor.close()
#         return cursor