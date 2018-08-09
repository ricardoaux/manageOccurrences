from django.contrib.auth.models import User
from rest_framework import serializers
from manageOccurrences.myapp.models import Occurrence


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class OccurrenceSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='author.username', read_only=True)
    username = serializers.CharField(source='author', read_only=True)

    class Meta:
        model = Occurrence
        fields = ('id', 'author', 'username', 'description', 'created', 'updated', 'state', 'category')

