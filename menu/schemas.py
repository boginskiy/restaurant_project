from typing import List
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
    submenus_count: int = 0
    dishes_count: int = 0






# -----
# id: Optional[int]
