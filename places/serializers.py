from places.models import Location, Zone, GeoTag
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('position', )


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zone
        fields = ('member', 'geotag', 'member_location', 'radius')


class GeotagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoTag
        fields = ('name', )