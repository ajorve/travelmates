from events.models import Journey, CheckIn
from rest_framework import serializers


class JourneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journey
        fields = ('name', 'member', 'zone',)


class CheckInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('member', 'journey', 'time', 'place', 'geotag', 'self.check_in')