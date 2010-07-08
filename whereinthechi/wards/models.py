from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class WardsException(Exception):
    """Base exception class for this model."""
    pass

class MultipleWardsException(WardsException):
    """Exception to be raised if a point can be found in more than one neighborhoods."""
    pass

class WardsManager(models.GeoManager):
    """Custom manager class to add some extra table-level methods."""
    def get_ward(self, lat, lng):
        """Get the ward for given coordinates."""
        pnt = Point(lat, lng, srid=4326)
        qs = self.filter(geom__intersects=pnt)
        if qs.count() == 1:
            return "%s" % qs[0]
        else:
            raise MultipleWardsException()
        
# This is based an auto-generated Django model module created by ogrinspect.
# python manage.py ogrinspect wards/data/Wards.shp Wards --multi --srid=102671 --mapping --name-field=ward

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
    geom = models.MultiPolygonField(srid=102671)
    objects = WardsManager()

    def __unicode__(self): return self.ward
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "Wards"

# Auto-generated `LayerMapping` dictionary for Wards model
wards_mapping = {
    'data_admin' : 'DATA_ADMIN',
    'perimeter' : 'PERIMETER',
    'ward' : 'WARD',
    'alderman' : 'ALDERMAN',
    'ward_class' : 'CLASS',
    'ward_phone' : 'WARD_PHONE',
    'hall_phone' : 'HALL_PHONE',
    'hall_offic' : 'HALL_OFFIC',
    'address' : 'ADDRESS',
    'edit_date1' : 'EDIT_DATE1',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'MULTIPOLYGON',
}
