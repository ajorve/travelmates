from django.db import models
from django.contrib.auth.models import AbstractUser
from geoposition.fields import GeopositionField
from phonenumber_field.modelfields import PhoneNumberField


class Member(AbstractUser):
    """
    Create Member class.
    """
    phone = PhoneNumberField()
    image = models.ImageField(upload_to='media', null=True)
    default_location = GeopositionField(null=False)

    def latest_location(self):
        last_location = self.check_ins.latest('place')
        return last_location

    def __str__(self):
        return str(self.username)
