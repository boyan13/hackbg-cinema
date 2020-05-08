from .controllers import CinemaController
from ..decorators import login_required
import time
import os


class CinemaViews:

    def __init__(self):
        self.controller = CinemaController()

    # Create a new reservation
    # Choose Movie -> Choose Day -> Choose Hour -> Choose seats -> Confirm

    @login_required
    def make_reservation(self):
        self.show_program()
        pr_id = input("\nEnter projection id: ")

        seats_map = self.controller.get_projection_seats(projection_id=pr_id)
        for s in seats_map:
            print(s)

        res_seats = self.controller.reserved_seats(projection_id=pr_id)
        user_seats = []
        tickets = int(input("Tickets count: "))
        if tickets >0:
            for t in range(tickets):
                while True:
                    pass
                    row = int(input("\nEnter row: "))
                    col = int(input("Enter column: "))

                    if (row, col) not in (res_seats + user_seats):
                        user_seats.append((row, col))
                        break
                    else:
                        print("Seat is taken.")
            commit_res = input("\nDo you wanna finish resarvation? y/n: ")
            if commit_res.lower() == "y":
                for s in user_seats:
                    self.controller.make_reservation(projection_id = pr_id, row=s[0], col=s[1])
                    print("Resarvation is completed.")
            else:
                print("Resarvation is canceled.")
        else:
            print("Resarvation is canceled.")
        os.system('cls' if os.name == 'nt' else 'clear')


    # Display all reservations and choose which to cancel

    @login_required
    def cancel_reservation(self):
        self.show_reservations()
        pr_id = input("\nEnter projection id: ")

        seats_map = self.controller.get_projection_seats(projection_id=pr_id)
        for s in seats_map:
            print(s)

        # res_seats = self.controller.reserved_seats(projection_id=pr_id)
        user_seats = self.controller.user_seats(projection_id=pr_id)
        cancel_seats = []

        if len(user_seats) != 0:

            tickets = int(input("Tickets count: "))
            if tickets >0:
                if tickets > len(user_seats):
                    tickets = len(user_seats)
                for t in range(tickets):
                    while True:
                        pass
                        row = int(input("\nEnter row: "))
                        col = int(input("Enter column: "))

                        if (row, col) in user_seats and (row, col) not in cancel_seats:
                            cancel_seats.append((row, col))
                            break
                        else:
                            print("Seat is not yours.\n Continue? y/n: ")
                            continue_opr = input()
                            if continue_opr.lower() == "n":
                                print("Resarvation is not canceled.")
                                return False
                commit_res = input("\nDo you wanna finish operation? y/n: ")
                if commit_res.lower() == "y":
                    for s in cancel_seats:
                        self.controller.delete_reserved_seat(projection_id = pr_id, row=s[0], col=s[1])
                        print("Resarvation is canceled.")
                else:
                    print("Resarvation is not canceled.")
            else:
                print("Resarvation is not canceled.")
        else:
            print("Resarvation not found.")
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display all reservations
    @login_required
    def print_reservations(self):
        id = self.controller.get_user_info()[0]
        reservations = self.controller.get_user_reservation(id)

        if len(reservations) == 0:
            print("No reservations.")
        else:
            for r in reservations:
                print("Row: {}, Col: {}, Movie: {}, Time: {}, Date: {}, Id: {}".format(r[0], r[1], r[2], r[3],r[4],r[6]))

        time.sleep(len(reservations))
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display projections info (the entire programm)
    def print_program(self):
        projections = self.controller.all_projections()
        for p in projections:
            print("Id: {}, Movie: {}, Time: {}, Date: {}, Seats: {}".format(p[3], p[0], p[1], p[2], p[4]))
        time.sleep(len(projections))
        os.system('cls' if os.name == 'nt' else 'clear')

    # Display all movies and ratings
    def print_movies(self):
        movies = self.controller.get_movies()
        for m in movies:
            print("Id: {}, Name: {}, Rating: {}".format(m[0], m[1], m[2]))
        time.sleep(len(movies))
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_program(self):
        projections = self.controller.all_projections()
        for p in projections:
            print("Id: {}, Movie: {}, Time: {}, Date: {}, Seats: {}".format(p[3], p[0], p[1], p[2], p[4]))

    def show_reservations(self):
        id = self.controller.get_user_info()[0]
        reservations = self.controller.get_user_reservation(id)

        if len(reservations) == 0:
            print("No reservations.")
        else:
            for r in reservations:
                print("Row: {}, Col: {}, Movie: {}, Time: {}, Date: {}, Id: {}, Projection id: {}".format(r[0], r[1], r[2], r[3],r[4],r[6], r[5]))
