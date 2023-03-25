from .models import User


def is_exist_user(user_id):
    """Функція перевірки унікальності користувача"""
    user = User.objects(user_id=user_id)
    if user:
        return True
    else:
        return False


def set_user(user_id, first_name, last_name):
    """Функція запису користувачів в БД"""
    user = User(user_id=user_id, first_name=first_name, last_name=last_name)
    user.save()


if __name__ == '__main__':
    pass
