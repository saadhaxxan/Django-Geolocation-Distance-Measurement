from django.shortcuts import render, get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm
from geopy import Photon
from geopy.distance import geodesic
from .utils import get_geo, get_zoom , get_center_coordinates
import folium

def calculate_distance_view(request):
    # obj = get_object_or_404(Measurement,id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocater = Photon(user_agent='measurements')

    ip = '101.53.254.73'
    country,city,lat,lon = get_geo(ip)
    # print(country,lon,lat,city)
    location = geolocater.geocode(city,timeout=10, exactly_one=True)
    pointA = (lat,lon)
    m = folium.Map(location=get_center_coordinates(lat,lon),zoom_start=8)
    folium.Marker([lat,lon],tooltip='Click here to learn more',popup=city['city'],icon=folium.Icon(color='blue')).add_to(m)
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
        print(distance)
        m = folium.Map(location=get_center_coordinates(lat,lon,d_lat,d_lon),zoom_start=get_zoom(distance))
        folium.Marker([lat,lon],tooltip='Click here to learn more',popup=city['city'],icon=folium.Icon(color='blue')).add_to(m)
        folium.Marker([d_lat,d_lon],tooltip='Click here to learn more',popup=destination,icon=folium.Icon(color='red',icon='cloud')).add_to(m)
        instance.save()
    m = m._repr_html_()
    context = {
        'form':form,
        'map':m
    }
    return render(request,'measurements/main.html',context)

def test(request):
    pass