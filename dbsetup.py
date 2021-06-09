############------------ CONFIGURATION 1/2 ------------############
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import null


Base = declarative_base()


############------------ CLASS ------------############
class Restaurant(Base):
    ############------------ TABLE INFO -------########
    __tablename__ = "restaurant"
    ############------------ MAPPER ------------#######
    name = Column(String(80))
    id = Column(Integer, primary_key=True)


############------------ CONFIGURATION 2/2 ------------############
engine = create_engine('sqlite://restaurantmenu.db')

Base.metadata.create_all(engine)
