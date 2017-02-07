from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all, name='all_fly'),
    # url(r'^(?P<number_id>[0-9])$', views.number, name='number'),
]
