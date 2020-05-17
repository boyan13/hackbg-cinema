import unittest

from cinema_app.users.models import UserModel
from cinema_app.cinema.movie_model import MovieModel
from cinema_app.cinema.projection_model import ProjectionModel
from cinema_app.cinema.reservation_model import ReservationModel


class TestValidation(unittest.TestCase):
    def test_movieValidation_with_none(self):
        movie = None
        exc = None
        try:
            MovieModel().validate_movie(movie)
        except Exception as e:
            exc = e
        self.assertEqual(str(exc), "Movie is not found.")

    def test_list_validation_with_none(self):
        elements = None

        res1 = MovieModel().validete_list_elements(elements)
        res2 = ProjectionModel().validete_list_elements(elements)
        res3 = ReservationModel().validete_list_elements(elements)

        self.assertEqual(res1, ["Nothing found."])
        self.assertEqual(res2, ["Nothing found."])
        self.assertEqual(res3, ["Nothing found."])

    def test_list_validation_with_elements(self):
        elements = []

        res1 = MovieModel().validete_list_elements(elements)
        res2 = ProjectionModel().validete_list_elements(elements)
        res3 = ReservationModel().validete_list_elements(elements)

        self.assertEqual(res1, [])
        self.assertEqual(res2, [])
        self.assertEqual(res3, [])

    def test_user_validation_with_correct_email_and_passwors(self):
        email = "silviV_pz98@abv.bg"
        password = "1ASaaopf32"

        self.assertTrue(UserModel().validate(email, password))

    def test_user_validation_with_incorrect_email_no_at(self):
        email = "silviV_pz98abv.bg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_no_point(self):
        email = "silviV_pz98@abvbg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_at_after_point(self):
        email = "silviV_pz98abv.@bg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_begins_with_at(self):
        email = "@silviV_pz98abv.bg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_ends_with_point(self):
        email = "silviV_pz98@abvbg."
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_two_at(self):
        email = "silviV_pz98@@abv.bg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_email_two_points(self):
        email = "silviV_pz98@abv..bg"
        password = "1ASaaopf32"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Invalid email.")

    def test_user_validation_with_incorrect_password_no_number(self):
        email = "silviV_pz98@abv.bg"
        password = "ASaaopfaaa"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Make sure your password has a number in it.")

    def test_user_validation_with_incorrect_password_no_upper_case(self):
        email = "silviV_pz98@abv.bg"
        password = "1aaopfaaa"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Make sure your password has a capital letter in it.")

    def test_user_validation_with_incorrect_password_less_then_8_letters(self):
        email = "silviV_pz98@abv.bg"
        password = "AS1paa"

        exc = None

        try:
            UserModel().validate(email, password)
        except Exception as e:
            exc = e

        self.assertEqual(str(exc), "Make sure your password is at lest 8 letters.")


if __name__ == '__main__':
    unittest.main()
