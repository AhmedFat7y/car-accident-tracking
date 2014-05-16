from django.forms import ModelForm
from mainapp.models import Vehicle
from mainapp.models import SensorsData

class VehicleForm(ModelForm):
     class Meta:
         model = Article
         fields = ['name', 'owner']

class SensorsDataForm(ModelForm):
     class Meta:
         model = SensorsData
         fields = ['longitude', 'latitude']