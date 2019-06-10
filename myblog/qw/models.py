from werkzeug.security import generate_password_hash, check_password_hash
from .db import login_manager, mongo


class User:
    user = None
    is_authenticated = True
    is_anonymous = False
    is_active = False

    def __init__(self, user):
        self.user = user
        self.is_active = True

    def get_id(self):
        return str(self.user['_id'])

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


@login_manager.user_loader
def loader_user(user_id):
    return User(mongo.db.user.find_one({'_id': user_id}))
