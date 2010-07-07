from django.test import TestCase

from neighborhoods.models import Neighborhoods
from django.contrib.gis.geos import Point
class SimpleTest(TestCase):
    def test_my_neighborhood(self):
        pnt = Point(-87.643078, 41.938840, srid=4326)
        #pnt_wkt = 'POINT(38.5847 56.3304)'
        #qs = Neighborhoods.objects.filter(geom__contains=pnt_wkt)
        qs = Neighborhoods.objects.filter(geom__intersects=pnt)
        print qs
        self.assertNotEqual(0, len(qs))



