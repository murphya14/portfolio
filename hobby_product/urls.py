from django.conf.urls import url, include
from .views import all_hobby_products

urlpatterns = [
    url(r'^$', all_hobby_products, name='all_hobby_products'),
]