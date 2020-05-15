# Internal Imports
from ..decorators import login_required
from .movie_gateway import MovieGateway
from .projection_gateway import ProjectionGateway
from .reservation_gateway import ReservationGateway


class CinemaController:
    def __init__(self):
        self.movie_gateway = MovieGateway()
        self.projection_gateway = ProjectionGateway()
        self.reservation_gateway = ReservationGateway()

    def get_movies(self):
        movies = self.movie_gateway.get_movies()
        return self.movie_gateway.model.validete_list_elements(movies)

    def get_all_projections(self, *, movie_id, order = "ASC"):
        # id ne e movie_id
        movie = self.movie_gateway.get_movie(movie_id)
        try:
            self.movie_gateway.model.validate_movie(movie)
        except Exception as e:
            return str(e)
        else:
            pr = self.projection_gateway.get_all_projections(movie_id, order)
            return self.projection_gateway.model.validate_list_elements(pr)

    def get_projections_by_date(set, *, movie_id, pr_date):
        movie = self.movie_gateway.get_movie(movie_id)
        try:
            self.movie_gateway.model.validate_movie(movie)
        except Exception as e:
            return str(e)  # may be return list???
        else:
            pr = self.projection_gateway.getl_projections_by_date(movie_id, pr_date)
            return self.projection_gateway.model.validate_list_elements(pr)

    def get_projection_seats(self, projection_id):
        seats = (self.projection_gateway.get_seats(projection_id))
        seats_map = []
        seats_map.append("   1 2 3 4 5 6 7 8 9 10")
        row_temp = ""
        for row in range(1, 11):
            row_temp = ""
            if row != 10:
                row_temp += "{}  ".format(row)
            else:
                row_temp += "{} ".format(row)

            for col in range(1, 11):
                if (row, col) in seats:
                    row_temp += "* "
                else:
                    row_temp += "- "
            seats_map.append(row_temp)
        return seats_map

    def reserved_seats(self, projection_id):
        return self.projection_gateway.get_seats(projection_id)

    def all_projections(self):
        pr = self.projection_gateway.all_projections()
        return self.projection_gateway.model.validete_list_elements(pr)

    @login_required
    def delete_reserved_seat(self, *, projection_id, row, col):
        u_id = self.movie_gateway.get_user_info()[0]
        self.reservation_gateway.delete_reservation(u_id=u_id, projection_id=projection_id, row=row, col=col)

    @login_required
    def make_reservation(self, *, projection_id, row, col):
        u_id = self.movie_gateway.get_user_info()[0]
        self.reservation_gateway.insert_reservation(u_id=u_id, projection_id=projection_id, row=row, col=col)

    @login_required
    def user_seats(self, projection_id):
        u_id = self.movie_gateway.get_user_info()[0]
        return self.projection_gateway.get_user_seats(u_id=u_id, projection_id=projection_id)

    @login_required
    def get_user_info(self):
        return self.movie_gateway.get_user_info()

    @login_required
    def get_user_reservation(self, r_id):
        u_id = self.movie_gateway.get_user_info()[0]
        return self.reservation_gateway.get_user_reservation(u_id)