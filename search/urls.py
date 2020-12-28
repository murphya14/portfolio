from django.conf.urls import url, include
from .views import do_search, category, rent, groups, private_lessons, summer_course, weekend

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url('rent/', rent, name='rent'),
    url('groups/', groups, name='groups'),
    url('private_lessons/', private_lessons, name='private_lessons'),
    url('summer_course/', summer_course, name='summer_course'),
    url('weekend/', weekend, name='weekend'),
]