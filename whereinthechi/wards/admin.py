from django.contrib.gis import admin
from models import Wards

admin.site.register(Wards, admin.OSMGeoAdmin)