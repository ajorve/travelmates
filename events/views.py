from rest_framework import viewsets
from django.shortcuts import render, redirect
from events.serializers import CheckInSerializer, JourneySerializer
from events.models import Journey, CheckIn
from django.contrib.auth.decorators import login_required


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


# @login_required
def app(request):
    context = {}
    return render(request, 'app/www/index.html', context)
