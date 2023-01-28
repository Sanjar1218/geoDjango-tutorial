from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Zipcode


class ZipcodeSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = Zipcode
        geo_field = "home"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'address')