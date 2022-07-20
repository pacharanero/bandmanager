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
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Song(TimeStampedModel):
    """
    Song model
    """
    title = models.CharField(max_length=300)
    original_artist = models.CharField(max_length=300, blank=True, default='')
    tempo = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=50, blank=True, default='')


class Tag(models.Model):
    """
    Tag model
    """
    text = models.CharField(max_length=30)
    group = models.CharField(max_length=30)


class Setlist(TimeStampedModel):
    """
    Setlist model
    """
    title = models.CharField(max_length=300)
    songs = models.ManyToManyField(Song, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)


class Band(models.Model):
    """
    Band model
    """
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300, blank=True, default='')
    phone = models.CharField()
    twitter = models.CharField(max_length=300, blank=True, default='')
    facebook = models.CharField(max_length=300, blank=True, default='')
    instagram = models.CharField(max_length=300, blank=True, default='')
    soundcloud = models.CharField(max_length=300, blank=True, default='')
    bandcamp = models.CharField(max_length=300, blank=True, default='')
    youtube = models.CharField(max_length=300, blank=True, default='')
    tags = models.ManyToManyField(Tag, blank=True)


class Gig(TimeStampedModel):
    """
    Gig model
    """
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    setlist = models.ManyToManyField(Setlist, blank=True)
    date = models.DateField
    tags = models.ManyToManyField(Tag, blank=True)
