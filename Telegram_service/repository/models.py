from datetime import datetime
from .db_connect import connect
from mongoengine import Document
from mongoengine.fields import BooleanField, DateTimeField, StringField, IntField


class User(Document):
    """Модель користувачів"""
    user_id = IntField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    created = DateTimeField(default=datetime.now())
    is_active = BooleanField(default=True)
