# Internal Imports
from .db import Database

# Third-Party Library Imports
from sqlalchemy.engine.reflection import Inspector


def login_required(func):
    d = Database()

    def wrapper(*args, **kwargs):
        inspector = Inspector.from_engine(d.engine)
        temp_u = False
        if "temp_user" in inspector.get_table_names():
            temp_u = True
        if temp_u:
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
