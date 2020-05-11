from ..db import Database
from .projection_model import ProjectionModel
from ..db_shema.projections import *


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel(pr_id=None, m_id=None, pr_date=None, pr_time=None)
        self.db = Database()

    def get_all_projections(self, *, movie_id, order):
        if order.upper() == "DESC":
            self.db.cursor.execute(SHOW_ALL_PROJECTIONS_D, (movie_id,))
        else:
            self.db.cursor.execute(SHOW_ALL_PROJECTIONS, (movie_id,))
        projections = self.db.cursor.fetchall()
        self.db.connection.commit()
        return projections

    def get_projections_by_date(set, *, movie_id, date):
        self.db.cursor.execute(SHOW_PROJECTIONS, (movie_id, date))
        projections = self.db.cursor.fetchall()
        self.db.connection.commit()
        return projections

    def all_projections(self):
        self.db.cursor.execute(GET_ALL_PROJECTIONS)
        pr = self.db.cursor.fetchall()
        self.db.connection.commit()
        return pr

    def get_seats(self, projection_id):
        self.db.cursor.execute(GET_SEATS, (projection_id,))
        seats = self.db.cursor.fetchall()
        self.db.connection.commit()
        return seats

    def get_user_seats(self, *, u_id, projection_id):
        data = (projection_id, u_id)
        self.db.cursor.execute(GET_USER_SEATS, data)
        seats = self.db.cursor.fetchall()
        self.db.connection.commit()
        return seats
