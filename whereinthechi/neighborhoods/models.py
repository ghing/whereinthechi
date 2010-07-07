# python manage.py  ogrinspect ./neighborhoods/data/Neighboorhoods.shp Neighborhoods --srid=4296 --mapping --name-field=pri_neigh
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

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
    objects = models.GeoManager()

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
