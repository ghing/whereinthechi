from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class CommunityAreasException(Exception):
    """Base exception class for this model."""
    pass

class MultipleCommunityAreasException(CommunityAreasException):
    """Exception to be raised if a point can be found in more than one community area."""
    pass

class CommunityAreasManager(models.GeoManager):
    """Custom manager class to add some extra table-level methods."""
    def get_community_area(self, lat, lng):
        """Get the community area for given coordinates."""
        pnt = Point(lat, lng, srid=4326)
        qs = CommunityAreas.objects.filter(geom__intersects=pnt)
        if qs.count() == 1:
            return "%s" % qs[0]
        else:
            #print qs
            raise MultipleCommunityAreasException()

# This is based on an auto-generated Django model module created by ogrinspect.
# python manage.py ogrinspect ./communityareas/data/Community_area.shp CommunityAreas --srid=102671 --mapping --name-field=community

class CommunityAreas(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    comarea_field = models.IntegerField()
    comarea_id = models.IntegerField()
    area_numbe = models.CharField(max_length=2)
    community = models.CharField(max_length=80)
    area_num_1 = models.CharField(max_length=5)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.PolygonField(srid=102671)
    objects = CommunityAreasManager()

    def __unicode__(self): return self.community

# Auto-generated `LayerMapping` dictionary for CommunityAreas model
communityareas_mapping = {
    'objectid' : 'OBJECTID',
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'comarea_field' : 'COMAREA_',
    'comarea_id' : 'COMAREA_ID',
    'area_numbe' : 'AREA_NUMBE',
    'community' : 'COMMUNITY',
    'area_num_1' : 'AREA_NUM_1',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
