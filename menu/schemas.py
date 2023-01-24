from typing import List, Any
from pydantic import BaseModel, validator, Field
from datetime import date
from typing import Optional


class Menu(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class Menu_OUT(Menu):
    id: int
    submenus_count: int = None
    dishes_count: int = None


class Submenus_OUT(Menu):
    id: int
    dishes_count: int = 0


class Dishes_IN(Menu):
    price: float = 0


class Dishes_OUT(Menu):
    id: int
    price: float = 0


# -----
# id: Optional[int]
