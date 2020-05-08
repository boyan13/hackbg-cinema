from .db import Database


def login_required(func):
    d = Database()
    def wrapper(*args, **kwargs):
        d.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='temp_user';")
        user = d.cursor.fetchone()
        d.connection.commit()
        if user is not None:
            return func(*args, **kwargs)
        else:
            raise Exception("First login!")
    return wrapper



@login_required
def nz(a):
    print(a)


def main():
    try:
        nz("AAAAAAAAAAAA")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
