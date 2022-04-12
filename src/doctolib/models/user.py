from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    user_type = models.CharField(max_length=50)
    geo_location = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_type(self):
        return self.type