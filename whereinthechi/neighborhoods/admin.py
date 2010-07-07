from django.contrib.gis import admin
from models import Neighborhoods

#admin.site.register(Neighborhoods, admin.GeoModelAdmin)
admin.site.register(Neighborhoods, admin.OSMGeoAdmin)