from django.db import models
from geoposition.fields import GeopositionField
from accounts.models import Member


class Location(models.Model):
    position = GeopositionField()

    def __str__(self):
        return str(self.position)


class GeoTag(models.Model):

    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    member = models.ManyToManyField(Member, related_name='members')
    geotag = models.ManyToManyField(GeoTag, related_name='zones')
    location_area = # (geo_location radius/polygon) name = models.CharField(max_length=100)
    member_location = models.ForeignKey(Location, null=False)

    def __str__(self):
        return self.location_area
