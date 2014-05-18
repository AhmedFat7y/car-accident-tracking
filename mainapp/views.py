from django.http import Http404
from django.shortcuts import render_to_response, render
from mainapp.models import Vehicle, SensorsData
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.html import escape
from mainapp import constants
from forms import SensorsDataForm
from django.contrib.auth.models import User


def format_vehicle_data(vehicleData):
  icon = 'img/'
  status = ''
  if vehicleData.status == constants.ON_FIRE or vehicleData.status == constants.ACCIDENT:
    icon += constants.STATUS_ICON_COLORS[vehicleData.status]
    status = constans.STATUS_CHOICES[vehicleData.status][1]
  elif vehicleData.speed < 60:
    icon += constants.SPEED_ICON_COLORS[constants.VER_SLOW]
    status = "very slow"
  elif vehicleData.speed >= 60 and vehicleData.speed <= 90:
    icon += constants.SPEED_ICON_COLORS[constants.SLOW]
    status = "slow"
  else :
    icon += constants.SPEED_ICON_COLORS[constants.FAST]
    status = "very slow"
  return {
    "long": vehicleData.longitude,
    "lat": vehicleData.latitude,
    "speed": vehicleData.speed,
    "status": status,
    "icon": icon
  }

def all_cars(request):
  allVehicles = Vehicle.objects.all()
  allVehiclesData = []
  for vehicle in allVehicles:
    vehicleData = vehicle.sensorsdata_set.order_by('-timestamp')
    if vehicleData:
      vehicleData = vehicleData[0]
    else:
      continue
    allVehiclesData.append(format_vehicle_data(vehicleData))
  data_dictionary = {"allVehiclesData": allVehiclesData};
  return render(request, 'index.html', dictionary=data_dictionary)
def index(request):
  if(request.user.is_authenticated()):
    allVehicles = request.user.vehicle_set.all()
  else:
    allVehicles = Vehicle.objects.all()
  allVehiclesData = []
  for vehicle in allVehicles:
    vehicleData = vehicle.sensorsdata_set.order_by('-timestamp')
    if vehicleData:
      vehicleData = vehicleData[0]
    else:
      continue
    allVehiclesData.append(format_vehicle_data(vehicleData))
  data_dictionary = {"allVehiclesData": allVehiclesData};
  return render(request, 'index.html', dictionary=data_dictionary)

def receive_data(request):
  form = SensorsDataForm(request.GET)
  if not form.is_valid():
    return Http404("")
  data = form.save(commit=False)
  user = User.objects.get(email=form.cleaned_data['owner_id'])
  vehicle = user.vehicle_set.get_or_create(pk=form.cleaned_data['vehicle_id'])
  data.vehicle = vehicle
  data.save()
  return HttpResponse()

