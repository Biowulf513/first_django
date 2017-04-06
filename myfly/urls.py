from django.conf.urls import url
from . import views

app_name = 'myfly'
urlpatterns = [
    url(r'^$', views.TableView.as_view(), name='table'),
    url(r'^flight/(?P<pk>[0-9]+)/$', views.FlightView.as_view(),
        name='flight'),
]