from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class CensusTractsException(Exception):
    """Base exception class for this model."""
    pass

class MultipleCensusTractsException(CensusTractsException):
    """Exception to be raised if a point can be found in more than one beat."""
    pass

class CensusTractsManager(models.GeoManager):
    """Custom manager class to add some extra table-level methods."""
    def get_census_tract(self, lat, lng):
        """Get the census tract number for given coordinates."""
        pnt = Point(lng, lat, srid=4326)
        qs = CensusTracts.objects.filter(geom__intersects=pnt)
        if qs.count() == 1:
            return "%s" % qs[0]
        else:
            #print qs
            raise MultipleCensusTractsException()

# This is based on an auto-generated Django model module created by ogrinspect.
# python manage.py ogrinspect ./censustracts/data/Census_Tracts.shp CensusTracts --srid=102671 --mapping --multi --name-field=census_tra

class CensusTracts(models.Model):
    objectid = models.IntegerField()
    census_tra = models.CharField(max_length=6)
    census_t_1 = models.CharField(max_length=11)
    tract_fips = models.CharField(max_length=5)
    tract_cent = models.FloatField()
    tract_ce_1 = models.FloatField()
    tract_ce_2 = models.FloatField()
    tract_ce_3 = models.FloatField()
    tract_comm = models.CharField(max_length=2)
    tract_numa = models.IntegerField()
    tract_cens = models.IntegerField()
    perimeter = models.FloatField()
    data_admin = models.FloatField()
    tract_crea = models.CharField(max_length=10)
    tract_cr_1 = models.DateField(null=True)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=102671)
    objects = CensusTractsManager()

    def __unicode__(self): return self.census_tra
    
    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "Census Tracts"

# Auto-generated `LayerMapping` dictionary for CensusTracts model
censustracts_mapping = {
    'objectid' : 'OBJECTID',
    'census_tra' : 'CENSUS_TRA',
    'census_t_1' : 'CENSUS_T_1',
    'tract_fips' : 'TRACT_FIPS',
    'tract_cent' : 'TRACT_CENT',
    'tract_ce_1' : 'TRACT_CE_1',
    'tract_ce_2' : 'TRACT_CE_2',
    'tract_ce_3' : 'TRACT_CE_3',
    'tract_comm' : 'TRACT_COMM',
    'tract_numa' : 'TRACT_NUMA',
    'tract_cens' : 'TRACT_CENS',
    'perimeter' : 'PERIMETER',
    'data_admin' : 'DATA_ADMIN',
    'tract_crea' : 'TRACT_CREA',
    'tract_cr_1' : 'TRACT_CR_1',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
