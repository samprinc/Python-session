from rest_framework import serializers
from .models import Sermon, Event, Ministry, HomepageContent, Livestream


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '_all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start_time', 'end_time', 'location',] 


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = '__all__'


class HomepageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageContent
        fields = '__all__'


class LivestreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestream
        fields = '__all__'
