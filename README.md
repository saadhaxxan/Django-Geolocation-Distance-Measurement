<div align="center">
<h1>Django Geolocation Distance Measurement</h1>
<img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" height="150px" width="250px">
<img src="https://miro.medium.com/max/480/1*YTnIluRNB5WWn-HhPIkoWQ.png" height="150px" width="250px">
<br>
<br>
</div>
<hr>
<h4>A django app to calculate distance between two points with folium maps and matrics<h4>

### Screenshot
<img src="screenshot.png">

## Installation steps

Clone the Repo and install the requirements

```
git clone https://github.com/saadhaxxan/Django-Geolocation-Distance-Measurement.git
cd Django-Geolocation-Distance-Measurement
pip install -r requirements.txt
```
### Get Geodatabases from Maxmindb
 - [Get from Here](https://www.maxmind.com/en/accounts/549107/geoip/downloads)
 - Paste them to geoip folder 
 - run the application

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Integrate into an Existing Application

### Add into installed Apps
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'measurements',
]
```

## Author
You can get in touch with me on my LinkedIn Profile:

#### Saad Hassan
[![LinkedIn Link](https://img.shields.io/badge/Connect-saadhaxxan-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/saadhaxxan)

You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-saadhaxxan-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/saadhaxxan)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

