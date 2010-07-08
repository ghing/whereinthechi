from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class NeighborhoodsException(Exception):
    """Base exception class for this model."""
    pass

class MultipleNeighborhoodsException(NeighborhoodsException):
    """Exception to be raised if a point can be found in more than one neighborhoods."""
    pass

class NeighborhoodsManager(models.GeoManager):
    """Custom manager class to add some extra table-level methods."""
    def get_neighborhood_name(self, lat, lng):
        """Get the neighborhood name for given coordinates."""
        pnt = Point(lat, lng, srid=4326)
        qs = Neighborhoods.objects.filter(geom__intersects=pnt)
        if qs.count() == 1:
            return "%s" % qs[0]
        else:
            raise MultipleNeighborhoodsException()

# This is based on an auto-generated Django model module created by ogrinspect.
# python manage.py  ogrinspect ./neighborhoods/data/Neighboorhoods.shp Neighborhoods --srid=102671 --mapping --name-field=pri_neigh

class Neighborhoods(models.Model):
    objectid = models.IntegerField()
    pri_neigh_field = models.CharField(max_length=3)
    pri_neigh = models.CharField(max_length=50)
    sec_neigh_field = models.CharField(max_length=3)
    sec_neigh = models.CharField(max_length=50)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.PolygonField(srid=102671)
    #geom = models.PolygonField(srid=4269)
    #geom = models.PolygonField(srid=4296)
    #geom = models.PolygonField(srid=3435) 
    
    #objects = models.GeoManager()
    objects = NeighborhoodsManager()
    
    def __unicode__(self): return self.pri_neigh

# Auto-generated `LayerMapping` dictionary for Neighborhoods model
neighborhoods_mapping = {
    'objectid' : 'OBJECTID',
    'pri_neigh_field' : 'PRI_NEIGH_',
    'pri_neigh' : 'PRI_NEIGH',
    'sec_neigh_field' : 'SEC_NEIGH_',
    'sec_neigh' : 'SEC_NEIGH',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
