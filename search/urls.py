from django.conf.urls import url, include
from .views import do_search, category, rent, groups, private_lessons, summer_course, weekend

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'rent/$', rent, name='rent'),
    url(r'^$', summer_course, name='summer_course'),
    url('groups/', groups, name='groups'),
    url('private_lessons/', private_lessons, name='private_lessons'),
    url('weekend/', weekend, name='weekend'),
]