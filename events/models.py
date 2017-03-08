from django.db import models
from accounts.models import Member
from places.models import Zone, GeoTag, Location

# Create your models here.


class Journey(models.Model):
    member = models.ManyToManyField(Member, through=CheckIn, related_name='members')
    check_in = models.DateTimeField()
    zone =
    geotag =


class CheckIn(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='check_ins')
    journey = models.ManyToOneRel(Journey, related_name='checked_into')
    time = models.DateTimeField()
    place = models.OneToOneField(Zone)
    tag = models.ManyToManyField(GeoTag, related_name='tags')

    def __str__(self):
        return self.place

    class Meta:
        ordering = ('time',)

