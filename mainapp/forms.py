from django import forms
from mainapp.models import Vehicle
from mainapp.models import SensorsData

class SensorsDataForm(forms.ModelForm):
  class Meta:
    model = SensorsData
    exclude = ['vehicle']
  owner_id = forms.EmailField()
  vehicle_id = forms.IntegerField()