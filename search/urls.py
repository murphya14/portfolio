  
from django.conf.urls import url
from .views import do_search, category

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url('<str:category>', category, name='category'),
]