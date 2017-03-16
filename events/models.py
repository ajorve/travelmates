from django.db import models
from datetime import datetime


# Create your models here.


class Journey(models.Model):
    name = models.CharField(max_length=15)
    member = models.ManyToManyField('accounts.Member', through='events.CheckIn', related_name='members')
    # check_in = models.DateTimeField()
    zone = models.ManyToManyField('places.Zone', related_name='zones')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class CheckIn(models.Model):
    member = models.ForeignKey('accounts.Member', on_delete=models.CASCADE, related_name='check_ins')
    journey = models.ForeignKey('events.Journey', related_name='checked_into')
    time = models.DateTimeField(null=False)
    place = models.OneToOneField('places.Zone')
    geotag = models.ManyToManyField('places.GeoTag', related_name='geotags')

    def timestamp(self):
        self.check_in = datetime.now()

    def __str__(self):
        return self.place

    class Meta:
        ordering = ('time',)

