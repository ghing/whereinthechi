# python manage.py ogrinspect wards/data/Wards.shp Wards --srid=4296 --mapping --name-field=ward
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Wards(models.Model):
    data_admin = models.FloatField()
    perimeter = models.FloatField()
    ward = models.CharField(max_length=4)
    alderman = models.CharField(max_length=60)
    ward_class = models.CharField(max_length=2)
    ward_phone = models.CharField(max_length=12)
    hall_phone = models.CharField(max_length=12)
    hall_offic = models.CharField(max_length=45)
    address = models.CharField(max_length=39)
    edit_date1 = models.CharField(max_length=10)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    #geom = models.PolygonField(srid=4296)
    geom = models.PolygonField(srid=102671)
    objects = models.GeoManager()

    def __unicode__(self): return self.ward

# Auto-generated `LayerMapping` dictionary for Wards model
wards_mapping = {
    'data_admin' : 'DATA_ADMIN',
    'perimeter' : 'PERIMETER',
    'ward_class' : 'WARD',
    'alderman' : 'ALDERMAN',
    'class' : 'CLASS',
    'ward_phone' : 'WARD_PHONE',
    'hall_phone' : 'HALL_PHONE',
    'hall_offic' : 'HALL_OFFIC',
    'address' : 'ADDRESS',
    'edit_date1' : 'EDIT_DATE1',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
