from django.conf.urls import url
from .views import create, auctions, detail, bid, auction_hobby_product

app_name = 'auctions'

urlpatterns = [
    url(r'^create/', create, name='create'),
    url(r'^auctions/', auctions, name='auctions'),
    url(r'^detail/', detail, name='detail'),
    url(r'^bid/(?P<id>\d+)', bid, name='bid'),
    url(r'^all_products/', auction_hobby_product, name='all_hobby_products')]
