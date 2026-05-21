from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class HouseMember(Base):
    __tablename__ = "house_members"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    house_id = Column(Integer, ForeignKey("houses.id"), primary_key=True)
    role = Column(String)  # admin or member