from django.core.management.base import BaseCommand, CommandError
from optparse  import make_option
import csv

from censustracts.models import CensusTracts, MultipleCensusTractsException
from communityareas.models import CommunityAreas, MultipleCommunityAreasException
from neighborhoods.models import Neighborhoods, MultipleNeighborhoodsException
from policebeats.models import PoliceBeats
from wards.models import Wards

class Command(BaseCommand):
    help = 'Add location columns to a comma separated value (CSV) file containing latitude and longitude.'

    option_list = BaseCommand.option_list + (
        make_option('--input-csv',
            action='store',
            dest='input_csv',
            help='Filename of input CSV file'),
        make_option('--output-csv',
            action='store',
            dest='output_csv',
            help='Filename of output CSV file'),
        make_option('--lat-col',
            action='store',
            dest='lat_col',
            help='Column of CSV file containing latitude'),
        make_option('--lng-col',
            action='store',
            dest='lng_col',
            help='Column of CSV file containing longitude'),
    )

    def handle(self, *args, **options):
        reader = csv.DictReader(open(options['input_csv']))
        fieldnames = reader.fieldnames + ['census_tract', 'community_area', 'neighborhood', 'police_beat', 'ward']
        writer = csv.DictWriter(open(options['output_csv'], 'w'), fieldnames=fieldnames)
        header_row = dict((field, field) for field in fieldnames)
        writer.writerow(header_row)
        for row in reader:
            lat = float(row[options['lat_col']])
            lng = float(row[options['lng_col']])
            newrow = dict((field, row[field]) for field in reader.fieldnames)
            
            try:
                newrow['census_tract'] = CensusTracts.objects.get_census_tract(lat, lng)
                newrow['community_area'] = CommunityAreas.objects.get_community_area(lat, lng)
                newrow['neighborhood'] = Neighborhoods.objects.get_neighborhood_name(lat, lng)
                newrow['police_beat'] = PoliceBeats.objects.get_beat_num(lat, lng)
                newrow['ward'] = Wards.objects.get_ward(lat, lng)
            except MultipleNeighborhoodsException:
                pass
            except MultipleCensusTractsException:
                pass
            except MultipleCommunityAreasException:
                pass

            writer.writerow(newrow)