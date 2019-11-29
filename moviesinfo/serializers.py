from moviesinfo.models import *
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

