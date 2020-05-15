# Third Party Library Imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self):
        self.Base = declarative_base()
        self.engine = create_engine("sqlite:///Cinema.db")
        self.sessionM = sessionmaker(bind=self.engine)
        self.session = self.sessionM()

    def create(self):
        # Model Imports
        from .users.models import UserModel, ClientModel
        from .cinema.movie_model import MovieModel
        from .cinema.projection_model import ProjectionModel
        from .cinema.reservation_model import ReservationModel

        tables = []

        if not self.engine.dialect.has_table(self.engine, UserModel.__tablename__):
            tables.append(UserModel.__table__)
        if not self.engine.dialect.has_table(self.engine, ClientModel.__tablename__):
            tables.append(ClientModel.__table__)
        if not self.engine.dialect.has_table(self.engine, MovieModel.__tablename__):
            tables.append(MovieModel.__table__)
        if not self.engine.dialect.has_table(self.engine, ProjectionModel.__tablename__):
            tables.append(ProjectionModel.__table__)
        if not self.engine.dialect.has_table(self.engine, ReservationModel.__tablename__):
            tables.append(ReservationModel.__table__)

        self.Base.metadata.create_all(self.engine, tables=tables)
