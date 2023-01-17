from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from routers import routers
from menu import models, schemas
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





# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @app.get('/api/v1/menus', response_model=schemas.Menu)
# def get_menu(db: Session = Depends(get_db)):
#     db_menu = crud.get_menu(db)
#     print('bbbb', db_menu)
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="Нет меню !")
#     return db_menu
#
# @app.post('/api/v1/menus', response_model=schemas.Menu)
# def add_menu(menu: schemas.Menu):
#     print(menu.dict())
#     return schemas.Menu(**menu.dict())


