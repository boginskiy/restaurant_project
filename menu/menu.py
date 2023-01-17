from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from typing import List
from . import service
from .schemas import Menu, Menu_OUT

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
    menu = service.create_menu(db, item)
    return menu


@router.patch("/menus/{menu_id}", response_model=Menu_OUT)
def patch_menu(item: Menu, menu_id: int, db: Session = Depends(get_db)):
    menu = service.patch_menu_detail(db, item, menu_id)
    return menu


@router.delete("/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = service.delete_menu_detail(db, menu_id)
    return menu
