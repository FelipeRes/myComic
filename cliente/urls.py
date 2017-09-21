from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from cliente import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
    url(r'^obra/(?P<pk>[0-9]+)/$', views.obra, name='obra'),
    url(r'^leitura/(?P<pk>[0-9]+)/$', views.leitura, name='leitura'),
    url(r'^minhas_obras/(?P<pk>[0-9]+)/$', views.minhas_obras, name='minhas_obras'),
    url(r'^login/$', views.login, name='login')
]
