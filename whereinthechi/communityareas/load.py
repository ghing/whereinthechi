import os
from django.contrib.gis.utils import LayerMapping
from models import CommunityAreas, communityareas_mapping

communityareas_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Community_area.shp'))

def run(verbose=True):
    lm = LayerMapping(CommunityAreas,  communityareas_shp, communityareas_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)