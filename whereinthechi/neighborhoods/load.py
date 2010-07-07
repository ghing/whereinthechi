import os
from django.contrib.gis.utils import LayerMapping
from models import Neighborhoods, neighborhoods_mapping

# These use unusual Spatial Reference System
# NAD 1983 StatePlane Illinois East FIPS 1201 Feet
# http://spatialreference.org/ref/esri/102671/
# This needs to be done before syncdb
#        add_postgis_srs(102671)
        
#management.call_command('syncdb')


neighborhoods_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Neighboorhoods.shp'))

def run(verbose=True):
    lm = LayerMapping(Neighborhoods,  neighborhoods_shp, neighborhoods_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
