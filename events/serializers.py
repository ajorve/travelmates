from events.models import Journey, CheckIn
from rest_framework import serializers


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ('name', 'member', 'zone',)


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ('member', 'journey', 'time', 'zone', 'geotag')