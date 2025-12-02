# File: Test/hi/models.py
# --- a/file:///d%3A/Test/Test/hi/models.py
from django.db import models


# ---------------------------
# 1. Sermons
# ---------------------------
class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=150)
    category= models.ForeignKey('SermonCategory', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    video_url = models.URLField(blank=True, null=True)
    audio_file = models.FileField(upload_to='sermons/audio/', blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} – {self.preacher}"

class SermonCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# ---------------------------
# 2. Events
# ---------------------------
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.title


# ---------------------------
# 3. Ministries
# ---------------------------
class Ministry(models.Model):
    name = models.CharField(max_length=200)
    leader = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ---------------------------
# 4. Homepage Content
# ---------------------------
class HomepageContent(models.Model):
    welcome_message = models.CharField(max_length=255)
    about_church = models.TextField()
    banner_image = models.ImageField(upload_to='homepage/', blank=True, null=True)

    def __str__(self):
        return "Homepage Content"


# ---------------------------
# 5. Livestream Links
# ---------------------------
class Livestream(models.Model):
    platform_name = models.CharField(max_length=100)  # e.g. YouTube, Facebook
    stream_url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.platform_name} Stream"
