# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from auction.models import Auction, hobby_product

class Post(models.Model):
    """
    A single post
    """
    hobby_product = models.OneToOneField(hobby_product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)


    def __unicode__(self):
        return self.title
