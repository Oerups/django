from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    user_type = models.CharField(max_length=50)
    geo_location = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_type(self):
        return self.type

class Appointment(models.Model):
    slot = models.ForeignKey(Slot)
    user_patient = models.ForeignKey(User)
    user_doctor = models.ForeignKey(User)
    confirmed = models.BooleanField(default=False)
    done = models.BooleanField(default=False)


class Slot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

class Ticket(models.Model):
   appointment = models.ForeignKey(Appointment)
   user = models.ForeignKey(User)
   description = models.TextField()

   def __str__(self):
       return self.headline