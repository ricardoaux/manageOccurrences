from django.contrib.auth.models import User
from rest_framework import serializers
from manageOccurrences.myapp.models import Occurrence


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # Modelo de dados para o utilizador. Predefinido pelo Django
        model = User
        # Campos enviados como resposta ao endpojnt /users
        fields = ('id', 'username', 'email', 'groups')


class OccurrenceSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='author.username', read_only=True)
    username = serializers.CharField(source='author', read_only=True)

    class Meta:
        # Modelo de dados a considerar. Ver models.py
        model = Occurrence
        # Campos enviados como resposta ao endpoint /occurrences
        fields = ('id', 'author', 'username', 'description', 'created', 'updated', 'state', 'category')

