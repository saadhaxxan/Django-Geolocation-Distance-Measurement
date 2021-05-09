from django.urls import path
from .views import *

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='calculate_distance'),
]
