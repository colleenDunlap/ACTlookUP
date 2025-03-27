from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Act(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    hero_image = models.ForeignKey('HeroImage', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Video(models.Model):
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    video_url = models.URLField()
   # video_engine = models.ForeignKey(VideoEngine, on_delete=models.SET_NULL, null=True)
    video_thumbnail = models.ImageField(upload_to='videos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""
Thought about adding video engines, but decided to keep it simple and not store business logic in database. Can parse from url if necessary.

class VideoEngine(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""
class Image(models.Model):
   # act = models.ManyToManyField(Act)
   #thought about making this many to many to reduce image storage, but wanted the speed of a foreign key.
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
