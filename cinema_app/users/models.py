import re


class UserModel:
    def __init__(self, *, id, email):
        self.id = id
        self.email = email

    @staticmethod
    def validate(email, password):
        count_at = email.count("@")
        count_point = email.count(".")

        if count_at != 1:
            raise Exception("Invalid email.")
        elif count_point != 1:
            raise Exception("Invalid email.")
        else:
            index_a = email.find("@")
            index_p = email.find(".")
            if index_a >= index_p - 1:
                raise Exception("Invalid email.")
            if index_a == 0 or index_p == len(email) - 1:
                raise Exception("Invalid email.")
        if len(password) < 8:
            raise Exception("Make sure your password is at lest 8 letters.")
        elif re.search('[0-9]', password) is None:
            raise Exception("Make sure your password has a number in it.")
        elif re.search('[A-Z]', password) is None:
            raise Exception("Make sure your password has a capital letter in it.")
        else:
            print("Your email and password are fine.")
            return True
        return False


def main():
    UserModel.validate("AZ@abv.bg")


if __name__ == '__main__':
    main()
