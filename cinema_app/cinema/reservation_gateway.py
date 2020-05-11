from ..db import Database
from .reservation_model import ReservationModel
from ..db_shema.reservations import *


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel(r_id=None, u_id=None, pr_id=None)
        self.db = Database()

    def get_user_reservation(self, u_id):
        self.db.cursor.execute(GET_USER_RESERVATIONS, (u_id,))
        r = self.db.cursor.fetchall()
        self.db.connection.commit()
        return r

    def insert_reservation(self, *, u_id, projection_id, row, col):
        reservation_data = (u_id, projection_id, row, col)
        self.db.cursor.execute(MAKE_RESERVETION, reservation_data)
        self.db.connection.commit()

    def delete_reservation(self, *, u_id, projection_id, row, col):
        reservation_data = (u_id, projection_id, row, col)
        self.db.cursor.execute(DELETE_RESERVATION, reservation_data)
        self.db.connection.commit()
