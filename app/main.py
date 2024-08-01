from fastapi import FastAPI
from .routers import user, task
from app.backend.db import engine
from app.models import Base

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(task.router)
