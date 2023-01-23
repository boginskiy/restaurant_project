
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from .models import Menu_DB, Sub_Menu_DB, Dish_DB
from .schemas import Menu

# Cделать классы, сделать расчет доп. полей


def get_menus(db: Session, menu_id=None):
    if not menu_id:
        return db.query(Menu_DB).all()

    menu = db.query(Menu_DB).get((menu_id,))

    if not menu:
        return JSONResponse(status_code=404,
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
        return JSONResponse(status_code=404,
                            content={"detail": "menu not found"})
    menu.title = item.dict()["title"]
    menu.description = item.dict()["description"]
    db.commit()
    db.refresh(menu)
    return menu


def delete_menu_detail(db: Session, menu_id: int):
    menu = db.query(Menu_DB).get((menu_id,))
    if menu == None:
        return JSONResponse(status_code=404,
                            content={"message": "User not found"})
    db.delete(menu)
    db.commit()
    return {"status": "true", "message": "The menu has been deleted"}


def get_submenus_detail(db: Session, menu_id: int, submenu_id=None):
    if not submenu_id:
        submenus = db.query(Sub_Menu_DB).filter(Sub_Menu_DB.menu_id == menu_id).all()
        return submenus
    submenus = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.id == submenu_id, Sub_Menu_DB.menu_id == menu_id).first()
    if not submenus:
        return JSONResponse(status_code=404,
                            content={"detail": "submenu not found"})
    return submenus


def create_submenu(db: Session, menu_id: int, item: Menu):
    new_submenus = Sub_Menu_DB(**item.dict(), menu=menu_id)
    db.add(new_submenus)
    db.commit()
    db.refresh(new_submenus)
    return new_submenus


def patch_submenu_detail(db: Session, item: Menu, submenu_id: int, menu_id: int):
    submenu = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.menu == menu_id, Sub_Menu_DB.id == submenu_id).first()
    if not submenu:
        return JSONResponse(status_code=404,
                            content={"detail": "submenu not found"})

    submenu.title = item.dict()["title"]
    submenu.description = item.dict()["description"]
    db.commit()
    db.refresh(submenu)
    return submenu


def delete_submenu_detail(db: Session, submenu_id: int, menu_id: int):
    submenu = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.menu == menu_id, Sub_Menu_DB.id == submenu_id).first()
    if not submenu:
        return JSONResponse(status_code=404,
                            content={"message": "User not found"})
    db.delete(submenu)
    db.commit()
    return {"status": "true", "message": "The submenu has been deleted"}


def get_dishes_list(db: Session, submenu_id: int, menu_id: int, dish_id=None):
    if not dish_id:
        res = db.query(Dish_DB).join(Sub_Menu_DB).filter(
            Dish_DB.submenu_id == submenu_id, Sub_Menu_DB.menu_id == menu_id).all()

        # res = db.query(Dish_DB).outerjoin(Sub_Menu_DB).all()

        # dishes = (i[0] for i in res)
        return res

# Перезапустить докер с БД




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
