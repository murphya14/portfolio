from django.conf.urls import url, include
from .views import product_review, add_review

urlpatterns = [
    url(r'^product_review/(?P<id>\d+)', product_review, name='product_review'),
    url(r'^add_review/(?P<id>\d+)',  add_review, name='add_review')
]