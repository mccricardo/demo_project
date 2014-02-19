from django.conf.urls import patterns, url
from demo_app import views

urlpattenrs = patterns('',
	url(r'^$', views.index, name=index))