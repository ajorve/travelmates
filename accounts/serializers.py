from rest_framework import serializers
from django.contrib.auth.models import Group
from accounts.models import Member

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('username', 'phone', 'email', 'image', 'default_location',)
