from .user_gateway import UserGateway, UserModel
import hashlib

class UserContoller:
    def __init__(self):
        self.user_gateway = UserGateway()

    def make_it_secret(self, password):
        return hashlib.sha512(password.encode()).hexdigest()

    def create_user(self, email, password):
        self.user_gateway.model.validate(email, password)
        hashpass = self.make_it_secret(password)
        self.user_gateway.create(email=email, password=hashpass)

        # send email
        # sync with Slack

    def get_user(self, *, email, password):
        hashpass = self.make_it_secret(password)
        raw_user = self.user_gateway.get_user(email=email, password=hashpass)
        if raw_user is None:
            raise Exception("User not found.")
        else:
            # TODO temp Table User_t return raw_user
            pass

    def show_movies(self):
        m = self.user_gateway.get_movies()
        for i in m:
            print(i)

    def show_all_projections(self, *, movie_id, order):
        try:
            pr = self.user_gateway.get_projectons(movie_id=movie_id, order=order)
        except Exception as e:
            print(e)
        else:
            for i in pr:
                print(i)

    def show_projections_date(self, *, movie_id, date):
        try:
            pr = self.user_gateway.get_projectons_by_date(movie_id=movie_id, date=date)
        except Exception as e:
            print(e)
        else:
            for i in pr:
                print(i)

    def show_projection_seats(self, projection_id):
        seats = (self.user_gateway.show_seats(projection_id))
        seats_map = "   1 2 3 4 5 6 7 8 9 10"
        for row in range(1,11):
            if row != 10:
                seats_map += "\n{}  ".format(row)
            else:
                seats_map += "\n{} ".format(row)
            for col in range (1,11):
                if (row, col) in seats:
                    seats_map += "* "
                else:
                    seats_map += "- "
        print(seats_map)
        return seats_map

    def reserved_seats(self, projection_id):
        return self.user_gateway.return_reserved_seats(projection_id)

    def delete_reserved_seat(self, *, projection_id, row, col):
        self.user_gateway.delete_reservation(projection_id=projection_id, row=row, col=col)

    def make_reservation(self, *, projection_id, row, col):
        self.user_gateway.insert_reservation(projection_id=projection_id, row=row, col=col)

    def user_seats(self, projection_id):
        return self.user_gateway.get_user_seats(projection_id=projection_id)
