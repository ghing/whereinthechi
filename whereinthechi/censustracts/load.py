import os
#from django.core import management
from django.contrib.gis.utils import LayerMapping, add_postgis_srs
from models import CensusTracts, censustracts_mapping

censustracts_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Census_Tracts.shp'))

def run(verbose=True):
    # These use unusual Spatial Reference System
    # NAD 1983 StatePlane Illinois East FIPS 1201 Feet
    # http://spatialreference.org/ref/esri/102671/
    # This needs to be done before syncdb
    #add_postgis_srs(102671)
    #management.call_command('reset', 'neighborhoods')


    lm = LayerMapping(CensusTracts,  censustracts_shp, censustracts_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)