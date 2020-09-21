from rest_framework import serializers
from ps.positions.models import Ship, Position

class ShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ship
        fields = ['imo', 'name']

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['imo', 'signal_time', 'lat', 'lon']