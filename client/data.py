from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import fromfile
import json

datafile = open('data.geojson', 'r')
data = json.load(datafile)
pnt = GEOSGeometry(json.dumps(data))
print(pnt.json)
# for object in objects['features']:
#     properties = object['properties']
#     geometry = object['geometry']
#     node_id = properties.get('id')
#     name = properties.get('name', 'no-name')
#     location = fromstr(geometry.get('coordinates'))
#     Zipcode(
#         address = 'home',
#         home = location
#         ).save(commit=True)