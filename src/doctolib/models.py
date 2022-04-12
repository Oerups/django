from django.contrib.auth.models import AbstractUser
from django.db import models


class Slot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)

class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    user_patient = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='patient')
    user_doctor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='doctor')
    confirmed = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    tickets = models.ForeignKey('Ticket', on_delete=models.SET_NULL, null=True)

class Ticket(models.Model):
   user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
   title = models.CharField(max_length=255)
   user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='tickets')

   def __str__(self):
       return self.headline

class User(AbstractUser):
    geo_location = models.ForeignKey('GeoLocation', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GeoLocation(models.Model):
    code_departement = models.CharField(max_length=255)
    nom_departement = models.CharField(max_length=255)
    code_region = models.CharField(max_length=255)
    nom_region = models.CharField(max_length=255)

    def __str__(self):
       return self.nom_departement + " " + self.code_departement + " " + self.nom_region + " " + self.code_region