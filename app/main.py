from fastapi import FastAPI
from app.database import Base, engine

from app.models.user import User
from app.models.house import House
from app.models.house_member import HouseMember

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "HouseMate API is running"}