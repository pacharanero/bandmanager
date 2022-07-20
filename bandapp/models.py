"""
Bandapp Models    
"""

# standard imports
from pyexpat import model
from uuid import uuid4

# third party imports
from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract class for timestamped models
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    """
    Tag model
    """
    group = models.CharField(max_length=30)
    text = models.CharField(max_length=30)


class Song(TimeStampedModel):
    """
    Song model
    """
    chart_url = models.URLField(blank=True, default='')
    key = models.CharField(max_length=50, blank=True, default='')
    notes = models.TextField(blank=True)
    original_artist = models.CharField(max_length=300, blank=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, related_name="songs")
    tempo = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    video_url = models.URLField(blank=True, default='')


class Setlist(TimeStampedModel):
    """
    Setlist model
    """
    description = models.TextField(blank=True)
    songs = models.ManyToManyField(Song, blank=True, related_name="setlists")
    tags = models.ManyToManyField(Tag, blank=True, related_name="setlists")
    title = models.CharField(max_length=300)


class Band(models.Model):
    """
    Band model
    """
    bandcamp = models.CharField(max_length=300, blank=True, default='')
    description = models.TextField(blank=True)
    facebook = models.CharField(max_length=300, blank=True, default='')
    instagram = models.CharField(max_length=300, blank=True, default='')
    location = models.CharField(max_length=300, blank=True, default='')
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=50, blank=True, default='')
    soundcloud = models.CharField(max_length=300, blank=True, default='')
    tags = models.ManyToManyField(Tag, blank=True, related_name="bands")
    twitter = models.CharField(max_length=300, blank=True, default='')
    youtube = models.CharField(max_length=300, blank=True, default='')


class Gig(TimeStampedModel):
    """
    Gig model
    """
    date = models.DateField
    description = models.TextField(blank=True)
    location = models.CharField(max_length=300)
    setlist = models.ManyToManyField(Setlist, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="gigs")
