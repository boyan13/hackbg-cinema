from .user_gateway import UserGateway


class UserContoller:
    def __init__(self):
        self.user_gateway = UserGateway()

    def create_user(self, email, password):
        self.user_gateway.create(email=email, password=password)

        # send email
        # sync with Slack

    def set_user(self, *, email, password):
        self.user_gateway.set_user(email=email, password=password)
