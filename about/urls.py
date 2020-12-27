from django.conf.urls import url, include                                                                                                                                                                                                                                                  
from .views import about, home

urlpatterns = [
    url(r'^', about, name='about'),
]