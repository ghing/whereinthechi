from django.test import TestCase

from neighborhoods.models import Neighborhoods
from django.contrib.gis.geos import Point

#from django.core import management
#from django.contrib.gis.utils import add_postgis_srs

#add_postgis_srs(102671)

class SimpleTest(TestCase):
    def setUp(self):
        #add_postgis_srs(102671)
        #management.call_command('reset', 'neighborhoods')
        pass
        
    def test_my_neighborhood(self):
        pnt = Point(-87.643078, 41.938840, srid=4326)
        #pnt_wkt = 'POINT(38.5847 56.3304)'
        #qs = Neighborhoods.objects.filter(geom__contains=pnt_wkt)
        qs = Neighborhoods.objects.filter(geom__intersects=pnt)
        print qs
        self.assertNotEqual(0, len(qs))