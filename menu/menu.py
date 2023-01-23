from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List
from . import service
from .schemas import Menu, Menu_OUT, Submenus_OUT, Dishes_OUT
from .models import *

router = APIRouter()


@router.get("/menus", response_model=List[Menu_OUT])
def get_menus_list(db: Session = Depends(get_db)):
    menus = service.get_menus(db)
    return menus


@router.get("/menus/{menu_id}", response_model=Menu_OUT)
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.get_menus(db, menu_id)
    return menu


@router.post("/menus", response_model=Menu_OUT)
def post_menu(item: Menu, db: Session = Depends(get_db)):
    new_menu = service.create_menu(db, item)
    return new_menu


@router.patch("/menus/{menu_id}", response_model=Menu_OUT)
def patch_menu(item: Menu, menu_id: int, db: Session = Depends(get_db)):
    menu = service.patch_menu_detail(db, item, menu_id)
    return menu


@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.delete_menu_detail(db, menu_id)
    return menu


@router.get("/menus/{menu_id}/submenus",
            response_model=List[Submenus_OUT])
def get_submenus_list(menu_id: int, db: Session = Depends(get_db)):
    submenus = service.get_submenus_detail(db, menu_id)
    return submenus


@router.post("/menus/{menu_id}/submenus",
             response_model=Submenus_OUT)
def post_submenu(item: Menu, menu_id: int, db: Session = Depends(get_db)):
    new_submenu = service.create_submenu(db, menu_id, item)
    return new_submenu


@router.get("/menus/{menu_id}/submenus/{submenu_id}",
            response_model=Submenus_OUT)
def get_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    submenu = service.get_submenus_detail(db, menu_id, submenu_id)
    return submenu


@router.patch("/menus/{menu_id}/submenus/{submenu_id}",
            response_model=Submenus_OUT)
def patch_submenu(menu_id: int,
                submenu_id: int,
                item: Menu,
                db: Session = Depends(get_db)):
    submenu = service.patch_submenu_detail(db, item, submenu_id, menu_id)
    return submenu


@router.delete("/menus/{menu_id}/submenus/{submenu_id}")
def patch_submenu(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    submenu = service.delete_submenu_detail(db, submenu_id, menu_id)
    return submenu


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes") # response_model=List[Dishes_OUT]
def get_dishes(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    dishes = service.get_dishes_list(db, submenu_id, menu_id)
    return dishes


# @router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
# def get_dish(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
#     dish = service.get_dishes_list(db, submenu_id, menu_id, dish_id)
#     return dish
