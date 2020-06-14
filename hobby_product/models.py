from __future__ import unicode_literals
from django.db import models
import numpy as np
from django.contrib.auth.models import User
from datetime import timedelta, datetime, timezone
from math import ceil
from django.utils import timezone
from django.db.models import Avg



class hobby_product(models.Model):

    ARTS_AND_CRAFT = 'Arts & Craft'
    MUSIC = 'music'
    GAMES = 'games'
    COLLECTORS = 'collectors'
    ACADEMIC = 'academic'
    NONE = 'NUL'
    SPORT = 'sport and outdoors'
    OTHER = 'other'
    CATEGORIES = (
        (NONE, 'Select a category'),
        (ARTS_AND_CRAFT, 'Arts & Craft'),
        (MUSIC, 'Music'),
        (GAMES, 'Games'),
        (COLLECTORS, 'Collectors'),
        (SPORT, 'Sport & outdoors'),
        (ACADEMIC, 'Academic & Educational'),
        (OTHER, 'other')
    )

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=100, choices=CATEGORIES, blank=False)
    date_added = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']
 
    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Hobby Products"
    

