from ..db import Database
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ProjectionModel:
    __tablename__ = "Projections"
    Id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey*"Movie.Id")
    type = Column(String)
    date = Column(String)
    hour = Column(String)


    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements
