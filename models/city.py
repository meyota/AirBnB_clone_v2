#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
