from django.conf.urls import url
from . import views
from myfly.views import table

urlpatterns = [
	url(r'^$', views.table, name='table'),
	url(r'^flight/', views.flight, name='flight'),
	# url(r'^route/[0-9]/$', views.route_info, name='route_info'),
]
