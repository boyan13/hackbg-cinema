# Internal Imports
from ..db import Database
from .movie_model import MovieModel
from .projection_model import ProjectionModel

# Third-Party Library Imports
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey


db = Database()


class ReservationModel(db.Base):
    __tablename__ = "Reservations"
    Id = Column(Integer, primary_key=True)
    projection_id = Column(Integer, ForeignKey(ProjectionModel.Id))
    user_id = Column(Integer, ForeignKey(MovieModel.Id))
    row = Column(Integer)
    col = Column(Integer)

    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements
