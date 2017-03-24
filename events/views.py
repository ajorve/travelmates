from rest_framework import viewsets, status
from rest_framework.response import Response
from events.serializers import CheckInSerializer, JourneySerializer
from events.models import Journey, CheckIn
from django.utils import timezone
from places.models import Zone, Location
from geoposition import Geoposition
from datetime import datetime, timedelta

# Create your views here.


class CheckInViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

    def list(self, request, *args, **kwargs):
        """
        GET Nearby_users, if NOT request.user
        :param request: GET
        :param args: Member, Geolocation, Time, Radius
        :return: Users checked-into radius of user within last 2 hours.
        """
        member = request.user
        time = timezone.now()
        past_timestamp = time - timedelta(hours=2)
        lat = request.GET['lat']
        lng = request.GET['lng']
        radius_meters = request.GET['radius']
        pos = Geoposition(lat, lng)
        location = Location(position=pos, created_time=time)
        zone = Zone(location=location, radius_meters=radius_meters)
        check_in = CheckIn(member=member, time=time, zone=zone, location=location)

        # Return USERS by timestamp within a range. (queryset)
        nearby_users = CheckIn.objects.filter(time__range=(past_timestamp, time)).exclude(member__pk=request.user.pk)
        serializer = CheckInSerializer(nearby_users, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def create(self, request, *args, **kwargs):
        """
        POST USER LOCATION AS CHECK-IN
        :param request: POST
        :param args: Member, Geolocation, Time, Radius
        :return: Users checked-into radius of user within last 2 hours.
        """
        member = request.user
        time = timezone.now()
        past_timestamp = time - timedelta(hours=2)
        lat = request.POST['lat']
        lng = request.POST['lng']
        radius_meters = request.POST['radius']

        pos = Geoposition(lat, lng)
        location = Location(position=pos, created_time=time)
        location.save()

        zone = Zone(location=location, radius_meters=radius_meters)
        zone.save()

        check_in = CheckIn(member=member, time=time, zone=zone, location=location)
        check_in.save()

        # Return USERS by timestamp within a range. (queryset)
        serializer = CheckInSerializer(check_in, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JourneyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer