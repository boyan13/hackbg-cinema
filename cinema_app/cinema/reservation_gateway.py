# Internal Imports
from ..db import Database
from ..db_shema.reservations import *
from ..users.models import Temp_user
from .movie_model import MovieModel
from .projection_model import ProjectionModel
from .reservation_model import ReservationModel


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel()
        self.db = Database()

    def get_user_reservation(self, u_id):
        r = self.db.session.query(ReservationModel.row,\
            ReservationModel.col,\
            MovieModel.name,\
            ProjectionModel.hour,\
            ProjectionModel.date,\
            ProjectionModel.Id,\
            ReservationModel.Id).filter(ReservationModel.user_id == u_id).filter(ProjectionModel.movie_id == MovieModel.Id).filter(ReservationModel.projection_id == ProjectionModel.Id).all()
        self.db.session.commit()
        return r

    def insert_reservation(self, *, u_id, projection_id, row, col):
        self.db.session.add_all([ReservationModel(projection_id=projection_id, user_id=u_id, row=row, col=col)])
        self.db.session.commit()

    def delete_reservation(self, *, u_id, projection_id, row, col):
        r_id = self.get_reservation_id(u_id=u_id, projection_id=projection_id, row=row, col=col)
        self.db.session.query(ReservationModel).filter(ReservationModel.Id == r_id).delete()
        self.db.session.commit()
    #     reservation_data = (u_id, projection_id, row, col)
    #     self.db.cursor.execute(DELETE_RESERVATION, reservation_data)
    #     self.db.connection.commit()

    def get_reservation_id(self, *, u_id, projection_id, row, col):
        r_id = self.db.session.query(ReservationModel.Id).filter(ReservationModel.user_id == u_id).filter(ReservationModel.projection_id == projection_id).filter(ReservationModel.row == row).filter(ReservationModel.col == col).first()
        return r_id[0]
