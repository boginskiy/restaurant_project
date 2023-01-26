from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from routers import routers
from menu import models
from core.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers)
