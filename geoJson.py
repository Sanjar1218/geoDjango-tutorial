import json
from django.contrib.gis.geos import GEOSGeometry, LinearRing
from spatialdata.models import Zipcode

def create_home():
    with open('export.geojson', 'r', encoding='utf-8') as f:
        data = json.load(f)

    features = data['features'][:1000]

    print(len(features))

    for feature in features:
        points = feature['geometry']
        properties = feature['properties']
        point = GEOSGeometry(json.dumps(points))
        print(type(point))
        zip1 = Zipcode(
            address = properties.get('name', 'Home'),
            home = point
        )
        zip1.save()
