from events.models import Journey, CheckIn
from rest_framework import serializers
from places.serializers import ZoneSerializer
from accounts.serializers import MemberSerializer


class JourneySerializer(serializers.ModelSerializer):

    class Meta:
        model = Journey
        fields = ('name', 'member', 'zone')


class CheckInSerializer(serializers.ModelSerializer):
    zone = ZoneSerializer()
    member = MemberSerializer()

    class Meta:
        model = CheckIn
        fields = ('member', 'journey', 'time', 'zone', 'geotag')
