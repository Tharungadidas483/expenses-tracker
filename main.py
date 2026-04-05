from fastapi import FastAPI
from database import Base, engine
import models
import routes.users as users
import routes.records as records

app = FastAPI(title="Expense Tracker API")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(records.router)


@app.get("/")
def home():
    return {"message": "API Running 🚀"}