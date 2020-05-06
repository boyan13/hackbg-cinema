from users.views import UserViews


def infinity():
	user_views = UserViews()
	while True:
		welcome(user_views)

def welcome(user_view):
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  3 - what i test\n  Input: '))
    user_views = user_view

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    if command == 3:
        return user_views.delete_seat()

    raise ValueError(f'Unknown command {command}.')
