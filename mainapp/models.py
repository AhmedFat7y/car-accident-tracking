from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from constants import STATUS_CHOICES, NORMAL

class Vehicle(models.Model):
  name = models.CharField(max_length=500)
  owner = models.ForeignKey(User)
  
  def __unicode__(self):
    return "Owner: %s, Vehicle Name: %s" %(self.owner.username, self.name)

class SensorsData(models.Model):
  longitude = models.DecimalField(max_digits=20, decimal_places=10)
  latitude = models.DecimalField(max_digits=20, decimal_places=10)
  speed = models.DecimalField(max_digits=20, decimal_places=10)
  temperature = models.DecimalField(max_digits=20, decimal_places=10)
  status = models.IntegerField(choices=STATUS_CHOICES, default=NORMAL)
  timestamp = models.DateField(auto_now_add=True)
  vehicle = models.ForeignKey(Vehicle)

  def __unicode__(self):
    return "longitude: %s, latitude: %s" % (self.longitude, self.latitude)