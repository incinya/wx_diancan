from django.db import models

# Create your models here.
import mongoengine


class Menu(mongoengine.Document):
    title = mongoengine.StringField(max_length=16)
    menuId = mongoengine.StringField(max_length=16)
    hot = mongoengine.StringField(max_length=16, default=None)
    bargin = mongoengine.StringField(max_length=16, default=None)
    active = mongoengine.BooleanField(max_length=16, default=False)
    all = mongoengine.StringField(max_length=16, default="所有菜品")
    price = mongoengine.IntField()
    id_ = mongoengine.IntField()
    num = mongoengine.IntField(default=1)
    img = mongoengine.FileField()
