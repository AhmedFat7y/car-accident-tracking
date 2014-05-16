from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SensorsData(models.Model):
  longitude = models.DecimalField(max_digits=10, decimal_places=10)
  latitude = models.DecimalField(max_digits=10, decimal_places=10)
  timestamp = models.DateField(auto_now_add=True)
  def __unicode__(self):
    return "longitude: %s, latitude: %s" % (self.longitude, self.latitude)
class Vehicle(models.Model):
  name = models.CharField(max_length=500)
  owner = models.ForeignKey(User)
  def __unicode__(self):
    return "Owner: %s, Vehicle Name: %s" %(self.owner.username, self.name)