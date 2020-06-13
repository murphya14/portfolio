from django.conf.urls import url, include
from .views import product_review, add_review

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', product_review, name='product_review'),
    url(r'^new/$',  add_review, name='add_review')
]