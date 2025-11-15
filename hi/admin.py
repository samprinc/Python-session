from django.contrib import admin
from .models import Sermon, Event, Ministry, HomepageContent, Livestream

admin.site.register(Sermon)
admin.site.register(Event)
admin.site.register(Ministry)
admin.site.register(HomepageContent)
admin.site.register(Livestream)
