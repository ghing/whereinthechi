from censustracts.models import CensusTracts
from communityareas.models import CommunityAreas
from neighborhoods.models import Neighborhoods
from policebeats.models import PoliceBeats
from wards.models import Wards

from django.http import HttpResponse
from django.utils import simplejson

def index(request, output):
    # BOOKMARK
    pass


def api(request, output):
    """
    Good test http://127.0.0.1:8000/api/json?latlng=41.938840,-87.643078 
    """
    response = None
        
    if "latlng" in request.GET:
        latlng = request.GET['latlng']
        (lat_str, lng_str) = latlng.split(',')
        lat = float(lat_str)
        lng = float(lng_str)
        
        response_data = {}
        response_data['status'] = "OK"
        response_data['census_tract'] = CensusTracts.objects.get_census_tract(lat, lng)
        response_data['community_area'] = CommunityAreas.objects.get_community_area(lat, lng)
        response_data['neighborhood'] = Neighborhoods.objects.get_neighborhood_name(lat, lng)
        response_data['police_beat'] = PoliceBeats.objects.get_beat_num(lat, lng)
        response_data['ward'] = Wards.objects.get_ward(lat, lng)
        
    return HttpResponse(simplejson.dumps(response_data), mimetype='application/json')