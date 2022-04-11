from django.contrib.auth.models import User
from django.db import models

class Appointment(models.Model):

    def __str__(self):
        return self.headline

class Tickets(models.Model):

   def __str__(self):
       return self.headline

class Practitioner(User):

   def __str__(self):
       return self.headline

class Patient(User):

   def __str__(self):
       return self.headline