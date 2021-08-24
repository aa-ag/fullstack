############------------ CONFIGURATION 1/2 ------------############
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


############------------ CLASS ------------############
class Restaurant(Base):
    ############------------ TABLE INFO -------########
    __tablename__ = 'restaurant'
    ############------------ MAPPER ------------#######
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


############------------ CLASS ------------############
class Menu(Base):
    ############------------ TABLE INFO -------########
    __tablename__ = 'menu_item'
    ############------------ MAPPER ------------#######
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        '''
         serializes formate to be able to send
         JSON objects.
        '''
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,

        }


############------------ CONFIGURATION 2/2 ------------############
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
