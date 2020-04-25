
from django.contrib import admin

from .models import Auction, Bid, hobby_product

admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(hobby_product)