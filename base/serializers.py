from .models import *
from rest_framework import serializers

class TrainSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Train
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):
    station = StationSerializer()
    class Meta:
        model = Platform
        fields = ['id', 'number', 'station']


class RouteSerializer(serializers.ModelSerializer):
    first_location = PlatformSerializer()
    second_location = PlatformSerializer()

    class Meta:
        model = Route
        fields = ['id', 'first_location', 'second_location', 'distance']


class TimeTableSerializer(serializers.ModelSerializer):
    departure =  PlatformSerializer()
    arrival = PlatformSerializer()

    class Meta:
        model = TimeTable
        fields = ['id', 'departure', 'arrival', 'schedule_type']


class JourneySerializer(serializers.ModelSerializer):
    time_table = TimeTableSerializer()
    
    class Meta:
        model = Journey
        fields = ['id', 'time_table', 'stop_count']


class JourneyRouteSerializer(serializers.ModelSerializer):
    train = TrainSerializer()
    journey = JourneySerializer()
    route = RouteSerializer()

    class Meta:
        model = JourneyRoute
        fields = ['id', 'train' , 'journey', 'route', 'departure_time']



