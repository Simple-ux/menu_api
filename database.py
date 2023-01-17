from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer,  String, update
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:feropulo@localhost:5432/menus"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    desc = Column(String)
    submenu_count = Column(Integer)
    dishes_count = Column(Integer)

class SubMenu(Base):
    __tablename__ = "submenu"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    desc = Column(String)
    dishes_count = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menu.id'))

class Dishes(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    desc = Column(String)
    price = Column(String)
    submenu_id = Column(Integer, ForeignKey('submenu.id'))


