from django.contrib.gis.geos import fromstr
from spatialdata.models import Zipcode
import json

datafile = open('data.geojson', 'r')
objects = json.load(datafile)
for object in objects['features']:
    properties = object['properties']
    geometry = object['geometry']
    node_id = properties.get('id')
    name = properties.get('name', 'no-name')
    location = fromstr(geometry.get('coordinates'))
    Zipcode(
        address = 'home',
        home = location
        ).save(commit=True)