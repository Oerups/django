from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    geo_location = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_type(self):
        return self.type

class Slot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    user_patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patient')
    user_doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='doctor')
    confirmed = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

class Ticket(models.Model):
   appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True)
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   description = models.TextField()

   def __str__(self):
       return self.headline