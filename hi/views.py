from rest_framework import viewsets
from rest_framework import filters # Ensure this is imported
from .models import Sermon, Event, Ministry, HomepageContent, Livestream
from .serializers import (
    SermonSerializer, EventSerializer, MinistrySerializer,
    HomepageContentSerializer, LivestreamSerializer
)

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all().order_by('-date')
    serializer_class = SermonSerializer
    # This activates the ?search= parameter
    filter_backends = [filters.SearchFilter] 
    # Looks for text in title, preacher name, OR category name
    search_fields = ['title', 'preacher', 'category__name'] 

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    # Add these two lines to enable search
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'location']

class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer
    # Add these two lines to enable search
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'leader']

# Homepage and Livestream usually don't need search, 
# but you can add it if you wish.
class HomepageContentViewSet(viewsets.ModelViewSet):
    queryset = HomepageContent.objects.all()
    serializer_class = HomepageContentSerializer

class LivestreamViewSet(viewsets.ModelViewSet):
    queryset = Livestream.objects.all()
    serializer_class = LivestreamSerializer