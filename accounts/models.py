from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField
from events.models import CheckIn


class Member(models.Model):
    """
    Create Member class.
    """
    user = models.OneToOneField(User)
    mobile_number = models.CharField(max_length=10)
    profile_image = models.ImageField()
    home_location = GeopositionField(null=False)

    def latest_location(self):
        location = self.check_ins.latest('place')
        return location

    class Meta:
        ordering = ['user']

    def __str__(self):
        return str(self.user)
