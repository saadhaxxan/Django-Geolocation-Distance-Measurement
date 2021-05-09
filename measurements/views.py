from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy import Photon
from geopy.distance import geodesic
from .utils import get_geo

def calculate_distance_view(request):
    # obj = get_object_or_404(Measurement,id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocater = Photon(user_agent='measurements')

    ip = '72.14.207.99'
    country,city,lat,lon = get_geo(ip)
    # print(country,lon,lat,city)
    location = geolocater.geocode(city,timeout=10, exactly_one=True)
    pointA = (lat,lon)
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocater.geocode(destination_,timeout=10, exactly_one=True)
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat,d_lon)
        distance = round(geodesic(pointA,pointB).km,2)
        instance.location = location
        instance.distance = distance
        instance.save()
    context = {
        'form':form,
        'distance':distance
    }
    return render(request,'measurements/main.html',context)

def test(request):
    pass