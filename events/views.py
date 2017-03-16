from rest_framework import viewsets
from events.serializers import CheckInSerializer, JourneySerializer
from events.models import Journey, CheckIn

# Create your views here.


class CheckInViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class JourneyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer