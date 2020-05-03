# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from datetime import timedelta, datetime, timezone
from math import ceil

class hobby_product(models.Model):

    ARTS_AND_CRAFT = 'Arts & Craft'
    MUSIC = 'music'
    GAMES = 'games'
    COLLECTORS = 'collectors'
    ACADEMIC = 'academic'
    NONE = 'NUL'
    SPORT = 'sport and outdoors'
    CATEGORIES = (
        (NONE, 'Select a category'),
        (MUSIC, 'Music'),
        (GAMES, 'Games'),
        (COLLECTORS, 'Collectors'),
        (SPORT, 'Sport & outdoors'),
        (ACADEMIC, 'Academic & Educational')
    )

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=11, choices=CATEGORIES, blank=False)
    date_added = models.DateTimeField()
 
    class Meta:
        hobby_product.objects.order_by('name', 'date_added')
        verbose_name_plural = "Hobby Products"

    '''Create a str of the model'''
    def __str__(self):
            return "Lot " + str(self.pk) + " " + self.name

# Auction duration in minutes
AUCTION_DURATION = 5

class Auction(models.Model):
    hobby_product = models.ForeignKey(hobby_product, unique=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, blank=True)
    min_value = models.IntegerField()
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET("(deleted)"),
                               blank=True,
                               null=True,
                               related_name="auction_winner",
                               related_query_name="auction_winner")
    final_value = models.IntegerField(blank=True, null=True)

    def resolve(self):
        if self.is_active:
            # If expired
            if self.has_expired():
                # Define winner
                highest_bid = Bid.objects.filter(auction=self).order_by('-amount').order_by('date').first()
                if highest_bid:
                    self.winner = highest_bid.bidder
                    self.final_value = highest_bid.amount
                self.is_active = False
                self.save()

    # Helper function that determines if the auction has expired
    def has_expired(self):
        now = datetime.now(timezone.utc)
        expiration = self.date_added + timedelta(minutes=AUCTION_DURATION)
        if now > expiration:
            return True
        else:
            return False

    # Returns the ceiling of remaining_time in minutes
    @property
    def remaining_minutes(self):
        if self.is_active:
            now = datetime.now(timezone.utc)
            expiration = self.date_added + timedelta(minutes=AUCTION_DURATION)
            minutes_remaining = ceil((expiration - now).total_seconds() / 60)
            return(minutes_remaining)
        else:
            return(0)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Auctions"

        """ Create a string of the model """
    def __str__(self):
        
        return "Auction " + str(self.pk) + " Hobby Product " + str(self.hobby_product.pk) + " " + self.hobby_product.name

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    # is_cancelled = models.BooleanField(default=False)
    date = models.DateTimeField('when the bid was made')

    class Meta:
        verbose_name_plural = 'Bids'

        """ Create a string of the model """
    def __str__(self):
        return "Bid " + str(self.pk) + " Auction " + str(self.auction.pk) + " " + self.auction.hobby_product.name