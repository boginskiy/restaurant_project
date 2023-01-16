from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Menu_DB(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # submenus =
