from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date
from typing import Optional


class Menu(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True

# Скорее всего это расчитываетя тут !
class Menu_OUT(Menu):
    id: int
    submenus_count: int = 0 # это !!!
    dishes_count: int = 0


class Submenus_OUT(Menu):
    id: int
    dishes_count: int = 0


class Dishes_OUT(Menu):
    id: int
    price: float = 0





# -----
# id: Optional[int]
