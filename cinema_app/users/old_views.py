from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()
        self.id = None
        self.email = None

    def login(self):
        email = input('Email: ')
        password = input('Password: ')
        try:
            self.id, self.email = self.controller.get_user(email=email, password=password)
            print("Welcome, hacker.")
        except Exception as e:
            print(str(e))

    def signup(self):
        email = input('Email: ')
        password = input('Password: ')
        try:
            self.controller.create_user(email=email, password=password)
        except Exception as e:
            print(str(e))

    def movie_list(self):
        self.controller.show_movies()

    def projection_list(self):
        m_id = input("Movie id: ")
        self.controller.show_all_projections(movie_id=m_id, order="DESC")

    def projecton_list_by_date(self):
        m_id = input("Movie id: ")
        date = input("date: ")
        self.controller.show_projections_date(movie_id=m_id, date=date)

    def show_seats(self):
        p_id = input("Projection id: ")
        self.controller.show_projection_seats(p_id)

    def reserve_seat(self):
        p_id = input("Projection id: ")
        self.controller.show_projection_seats(p_id)
        tickets = int(input("Tickets count: "))
        seats = []
        r_seats = self.controller.reserved_seats(p_id)
        for i in range(tickets):
            one_seat= True
            while one_seat:
                seat_row = int(input("Enter seat's row: "))
                seat_col = int(input("Enter seat's col: "))
                if (seat_row, seat_col) in r_seats or (seat_row, seat_col) in seats:
                    print("seats are taken")
                else:
                    seats.append((seat_row, seat_col))
                    break

        commit_r = input("Finish reservashion? y/n: ")
        if commit_r.lower() == "y":
            for s in seats:
                self.controller.make_reservation(projection_id=p_id, row=s[0], col=s[1])
        else:
            print("Resercation is canceled.")
    def delete_seat(self):
        p_id = input("Projection id: ")
        self.controller.show_projection_seats(p_id)
        tickets = int(input("Tickets count: "))
        seats = []
        r_seats = self.controller.user_seats(p_id)
        for i in range(tickets):
            one_seat= True
            while one_seat:
                seat_row = int(input("Enter seat's row: "))
                seat_col = int(input("Enter seat's col: "))
                if (seat_row, seat_col) in r_seats and (seat_row, seat_col) not in seats:
                    seats.append((seat_row, seat_col))
                    break
                else:
                    print("These seats are not yours")

        commit_r = input("Finish reservashion? y/n: ")
        if commit_r.lower() == "y":
            for s in seats:
                self.controller.delete_reserved_seat(projection_id=p_id, row=s[0], col=s[1])
        else:
            print("Resercation is canceled.")
