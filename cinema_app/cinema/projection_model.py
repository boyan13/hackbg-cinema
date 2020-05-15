from ..db import Database
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .movie_model import MovieModel


db = Database()


class ProjectionModel(db.Base):
    __tablename__ = "ProjectionModel"
    Id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(MovieModel.Id))
    type = Column(String)
    date = Column(String)
    hour = Column(String)
    # movie = relationship(ProjectionModel, backref=MovieModel)


    def validete_list_elements(self, elements):
        if elements is None:
            return ["Nothing found."]
        return elements

db.Base.metadata.create_all(db.engine, tables=[ProjectionModel.__table__])
