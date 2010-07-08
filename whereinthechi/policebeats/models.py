from django.contrib.gis.db import models

from django.contrib.gis.geos import Point

class PoliceBeatsException(Exception):
    """Base exception class for this model."""
    pass

class MultiplePoliceBeatsException(PoliceBeatsException):
    """Exception to be raised if a point can be found in more than one beat."""
    pass

class PoliceBeatsManager(models.GeoManager):
    """Custom manager class to add some extra table-level methods."""
    def get_beat_num(self, lat, lng):
        """Get the beat number for given coordinates."""
        pnt = Point(lat, lng, srid=4326)
        qs = PoliceBeats.objects.filter(geom__intersects=pnt)
        if qs.count() == 1:
            return "%s" % qs[0]
        else:
            raise MultiplePoliceBeatsException()

# This is based on an auto-generated Django model module created by ogrinspect.
# python manage.py ogrinspect ./policebeats/data/cpd_beats.shp PoliceBeats --srid=102671 --mapping --name-field=beat_num

class PoliceBeats(models.Model):
    objectid = models.IntegerField()
    district = models.CharField(max_length=2)
    sector = models.CharField(max_length=1)
    beat = models.CharField(max_length=1)
    beat_num = models.CharField(max_length=4)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.PolygonField(srid=102671)
    objects = PoliceBeatsManager()

    def __unicode__(self): return self.beat_num
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "Police Beats"

# Auto-generated `LayerMapping` dictionary for PoliceBeats model
policebeats_mapping = {
    'objectid' : 'OBJECTID',
    'district' : 'DISTRICT',
    'sector' : 'SECTOR',
    'beat' : 'BEAT',
    'beat_num' : 'BEAT_NUM',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
