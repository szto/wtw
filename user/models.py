from django.db import models
from enum import Enum

class Gender(Enum):
    MALE = 'M'
    FEMAIL = 'F'

    @classmethod
    def choices(cls):
        return [(tag, tag.value) for tag in Gender]

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=3, choices = Gender.choices())

    class Meta:
        db_table = 'users'

class UserOpion(models.Model):
    hate_hot = models.BooleanField(default = False)
    hate_cold = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users_option'


