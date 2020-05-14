from ..db import Database
from .projection_model import ProjectionModel
from .movie_model import MovieModel
from .reservation_model import ReservationModel
from ..db_shema.projections import *


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel()
        self.db = Database()

    # def get_all_projections(self, *, movie_id, order):
    #     projections = []
    #     if order.lower() == "desc":
    #         projections = self.db.session.query.filter(ProjectionModel.movie_id == movie_id).order(desc(ProjectionModel.date)).all()
    #     else:
    #          projections = self.db.session.query.filter(ProjectionModel.movie_id == movie_id).order(asc(ProjectionModel.date)).all()

    #     return projections

    # def get_projections_by_date(set, *, movie_id, date):
    #     self.db.cursor.execute(SHOW_PROJECTIONS, (movie_id, date))
    #     projections = self.db.cursor.fetchall()
    #     self.db.connection.commit()
    #     return projections

    def all_projections(self):
        pr = self.db.session.query(ProjectionModel).all()
        self.db.session.commit()
        # self.db.cursor.execute(GET_ALL_PROJECTIONS)
        # pr = self.db.cursor.fetchall()
        # self.db.connection.commit()
        return pr

    # def get_seats(self, projection_id):
    #     seats = self.db.session.query(ReservationModel.row, ReservationModel.col).filter(ReservationModel.projection_id == projection_id).all()
    #     self.db.session.commit()
    #     return seats

    # def get_user_seats(self, *, u_id, projection_id):
    #     seats = self.db.session.query(ReservationModel.row, ReservationModel.col).filter(ReservationModel.projection_id == projection_id, ReservationModel.user_id = u_id ).all()
    #     self.db.session.commit()
    #     return seats
