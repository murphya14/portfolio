from django.conf.urls import url, include
from .views import about_surf

urlpatterns = [
    url(r'^$', about_surf, name='about_surf'),
]