from django.conf.urls import url, include
from .views import do_search, category, rent

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^category/(?P<category>[A-Za-z]+)', category, name="category"),
    url('rent/', rent, name='rent'),
    url('groups/', groups, name='groups'),
    url('private_lessons/', private_lessons, name='private_lessons'),
    url('summer/', summer, name='summer'),
    url('weekend/', weekend, name='weekend'),
]