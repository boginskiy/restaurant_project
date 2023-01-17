from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .models import Menu_DB
from .schemas import Menu


def get_menus(db: Session, menu_id=None):
    if not menu_id:
        return db.query(Menu_DB).all()
    menu = db.query(Menu_DB).get((menu_id,))
    if not menu:
        return JSONResponse(
            status_code=404,
            content={"detail": "menu not found"})
    return menu


def create_menu(db: Session, item: Menu):
    menu = Menu_DB(**item.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def patch_menu_detail(db: Session, item: Menu, menu_id: int):
    menu = db.query(Menu_DB).get((menu_id,))
    if menu == None:
        return JSONResponse(
            status_code=404,
            content={"detail": "menu not found"})
    menu.title = item.dict()["title"]
    menu.description = item.dict()["description"]
    db.commit()
    db.refresh(menu)
    return menu


def delete_menu_detail(db: Session, menu_id: int):
    menu = db.query(Menu_DB).get((menu_id,))
    if menu == None:
        return JSONResponse(
            status_code=404,
            content={"message": "User not found"})
    db.delete(menu)
    db.commit()
    return {"status": "true", "message": "The menu has been deleted"}






# Бывший crud
# from sqlalchemy.orm import Session
# from menu import models, schemas
#
#
# def get_menu(db: Session):
#     print(db.query(models.Menu_DB).filter(models.Menu_DB.id == 1))
#     return db.query(models.Menu_DB).filter(models.Menu_DB.id == 1)
#
#
# def crate_menu(db: Session, menu: schemas.Menu):
#     db_menu = models.Menu_DB(title=menu.title, description=menu.description)
#     db.add(db_menu)
#     db.commit()
#     db.refresh(db_menu)
#     return db_menu

# @app.get("/api/users/{id}")
# def get_person(id, db: Session = Depends(get_db)):
#     # получаем пользователя по id
#     person = db.query(Person).filter(Person.id == id).first()
#     # если не найден, отправляем статусный код и сообщение об ошибке
#     if person == None:
#         return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
#     # если пользователь найден, отправляем его
#     return person
