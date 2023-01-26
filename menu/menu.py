from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List
from . import service
from .schemas import Menu, Menu_OUT, Submenus_OUT, Dishes_OUT, Dishes_IN

router = APIRouter()


@router.get("/menus", response_model=List[Menu_OUT])
def get_menus(db: Session = Depends(get_db)):
    menus = service.read_menus(db)
    return menus


@router.get("/menus/{menu_id}", response_model=Menu_OUT)
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.read_menus(db, menu_id)
    return menu


@router.post("/menus", response_model=Menu_OUT)
def post_menu(item: Menu, db: Session = Depends(get_db)):
    new_menu = service.create_menu(db, item)
    return new_menu


@router.patch("/menus/{menu_id}", response_model=Menu_OUT)
def patch_menu(item: Menu, menu_id: int, db: Session = Depends(get_db)):
    menu = service.update_menu(db, item, menu_id)
    return menu


@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    message = service.drop_menu(db, menu_id)
    return message


@router.get("/menus/{menu_id}/submenus",
            response_model=List[Submenus_OUT])
def get_submenus(menu_id: int, db: Session = Depends(get_db)):
    submenus = service.read_submenus(db, menu_id)
    return submenus


@router.post("/menus/{menu_id}/submenus",
             response_model=Submenus_OUT)
def post_submenu(item: Menu, menu_id: int, db: Session = Depends(get_db)):
    new_submenu = service.create_submenu(db, menu_id, item)
    return new_submenu


@router.get("/menus/{menu_id}/submenus/{submenu_id}",
            response_model=Submenus_OUT)
def get_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    submenu = service.read_submenus(db, menu_id, submenu_id)
    return submenu


@router.patch("/menus/{menu_id}/submenus/{submenu_id}",
              response_model=Submenus_OUT)
def patch_submenu(menu_id: int, submenu_id: int,
                item: Menu, db: Session = Depends(get_db)):
    submenu = service.update_submenu(db, item, submenu_id, menu_id)
    return submenu


@router.delete("/menus/{menu_id}/submenus/{submenu_id}")
def delete_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    message = service.drop_submenu(db, submenu_id, menu_id)
    return message


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes",
            response_model=List[Dishes_OUT])
def get_dishes(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    dishes = service.read_dishes(db, submenu_id, menu_id)
    return dishes


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
            response_model=Dishes_OUT)
def get_dish(menu_id: int, submenu_id: int,
             dish_id: int, db: Session = Depends(get_db)):
    dish = service.read_dishes(db, submenu_id, menu_id, dish_id)
    return dish


@router.post("/menus/{menu_id}/submenus/{submenu_id}/dishes",
             response_model=Dishes_OUT)
def post_dish(
        menu_id: int, submenu_id: int,
        item: Dishes_IN, db: Session = Depends(get_db)):
    dish = service.create_dish(db, item, submenu_id, menu_id)
    return dish


@router.patch("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
             response_model=Dishes_OUT)
def patch_dish(
        menu_id: int, submenu_id: int, dish_id: int,
        item: Dishes_IN, db: Session = Depends(get_db)):
    dish = service.update_dish(db, item, submenu_id, menu_id, dish_id)
    return dish


@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(menu_id: int, submenu_id: int, dish_id: int,
                db: Session = Depends(get_db)):
    message = service.drop_dish(db, menu_id, submenu_id, dish_id)
    return message
