from sqlalchemy import Column, Integer, String, ForeignKey, Float, select, func
from core.database import Base
from sqlalchemy.orm import relationship, column_property


class Dish_DB(Base):
    __tablename__ = 'dish'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))
    price = Column(Float(precision=2))
    submenu_id = Column(Integer, ForeignKey("submenu.id"))
    submenu = relationship("Sub_Menu_DB")


class Sub_Menu_DB(Base):
    __tablename__ = 'submenu'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))
    menu_id = Column(Integer, ForeignKey("menu.id"))
    menu = relationship("Menu_DB")

    dishes_count = column_property(
        select([func.count(Dish_DB.id)]).where(
            Dish_DB.submenu_id == id).scalar_subquery())


class Menu_DB(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(150))
    description = Column(String(450))

    submenus_count = column_property(
        select([func.count(Sub_Menu_DB.id)]).where(
            Sub_Menu_DB.menu_id == id).scalar_subquery())

    dishes_count = column_property(
        select([func.count(Dish_DB.id)]).where(
            Dish_DB.submenu_id == Sub_Menu_DB.id,
            Sub_Menu_DB.menu_id == id).scalar_subquery())
