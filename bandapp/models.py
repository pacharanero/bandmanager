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
    original_artist = models.CharField(max_length=300)
    tempo = models.IntegerField(max_length=4)
    key = models.CharField(max_length=50)


class Setlist(TimeStampedModel):
    """
    Setlist model
    """
    title = models.CharField(max_length=300)
    songs = models.ManyToManyField(Song)
