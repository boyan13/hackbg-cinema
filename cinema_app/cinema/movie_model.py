# Internal Imports
from ..db import Database

# Third-Party Library Imports
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


db = Database()


class MovieModel(db.Base):
    __tablename__ = "Movies"
    Id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements

    def validate_movie(self, movie):
        if movie is None:
            raise Exception("Movie is not found.")
