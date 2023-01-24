from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from .models import Menu_DB, Sub_Menu_DB, Dish_DB
from .schemas import Menu, Dishes_IN

# Cделать ООП стиль

def read_menus(db: Session, menu_id=None):
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


def update_menu(db: Session, item: Menu, menu_id: int):
    menu = db.query(Menu_DB).get((menu_id,))
    if menu == None:
        return JSONResponse(status_code=404,
                            content={"detail": "menu not found"})
    menu.title = item.dict()["title"]
    menu.description = item.dict()["description"]
    db.commit()
    db.refresh(menu)
    return menu


def drop_menu(db: Session, menu_id: int):
    menu = db.query(Menu_DB).get((menu_id,))
    if menu == None:
        return JSONResponse(status_code=404,
                            content={"message": "User not found"})
    db.delete(menu)
    db.commit()
    return {"status": "true", "message": "The menu has been deleted"}


def read_submenus(db: Session, menu_id: int, submenu_id=None):
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


def update_submenu(db: Session, item: Menu, submenu_id: int, menu_id: int):
    submenu = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.menu_id == menu_id, Sub_Menu_DB.id == submenu_id).first()
    if not submenu:
        return JSONResponse(status_code=404,
                            content={"detail": "submenu not found"})

    submenu.title = item.dict()["title"]
    submenu.description = item.dict()["description"]
    db.commit()
    db.refresh(submenu)
    return submenu


def drop_submenu(db: Session, submenu_id: int, menu_id: int):
    submenu = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.menu_id == menu_id, Sub_Menu_DB.id == submenu_id).first()
    if not submenu:
        return JSONResponse(status_code=404,
                            content={"message": "User not found"})
    db.delete(submenu)
    db.commit()
    return {"status": "true", "message": "The submenu has been deleted"}


def read_dishes(db: Session, submenu_id: int, menu_id: int, dish_id=None):
    if not dish_id:
        dishes = db.query(Dish_DB).join(Sub_Menu_DB).filter(
            Dish_DB.submenu_id == submenu_id, Sub_Menu_DB.menu_id == menu_id).all()
        return dishes

    dish = db.query(Dish_DB).join(Sub_Menu_DB).filter(Dish_DB.id == dish_id,
        Dish_DB.submenu_id == submenu_id, Sub_Menu_DB.menu_id == menu_id).first()

    if not dish:
        return JSONResponse(status_code=404,
                            content={"detail": "dish not found"})
    return dish


def create_dish(db: Session, item: Dishes_IN, submenu_id: int, menu_id: int):
    submenu = db.query(Sub_Menu_DB).filter(
        Sub_Menu_DB.menu_id == menu_id, Sub_Menu_DB.id == submenu_id).first()
    if not submenu:
        return JSONResponse(status_code=404,
                            content={"detail": "submenu and menu not correct"})

    new_dish = Dish_DB(**item.dict(), submenu_id=submenu_id)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


def update_dish(db: Session, item: Dishes_IN,
                submenu_id: int, menu_id: int, dish_id: int):

    dish = db.query(Dish_DB).join(Sub_Menu_DB).filter(Dish_DB.id == dish_id,
        Dish_DB.submenu_id == submenu_id, Sub_Menu_DB.menu_id == menu_id).first()
    if not dish:
        return JSONResponse(status_code=404,
                            content={"detail": "dish not found"})

    dish.title = item.dict()["title"]
    dish.description = item.dict()["description"]
    dish.price = item.dict()["price"]
    db.commit()
    db.refresh(dish)
    return dish
