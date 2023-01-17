from sqlalchemy import Column, Integer, String, ForeignKey, Float
from core.database import Base
from sqlalchemy.orm import relationship


class Menu_DB(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))


class Sub_Menu_DB(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))
    menu = Column(Integer, ForeignKey("menu.id"))
    menu_id = relationship("Menu_DB")


class Dish_DB(Base):
    __tablename__ = 'dish'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))
    price = Column(Float(precision=2))
    submenu = Column(Integer, ForeignKey("submenu.id"))
    submenu_id = relationship("Sub_Menu_DB")
