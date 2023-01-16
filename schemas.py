from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date
from typing import Optional


class Menu(BaseModel):
    id: Optional[int] = None
    title: str = None
    description: str = None

    class Config:
        orm_model=True


# class MenuOut(Menu):
#     submenus_count: int = 0
#     dishes_count: int = 0
