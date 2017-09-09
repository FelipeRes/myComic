from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^perfil/$', views.PerfilList.as_view(), name=views.PerfilList.name),
    url(r'^perfil/create/$', views.PerfilCreate.as_view(), name=views.PerfilCreate.name),
    url(r'^perfil/(?P<pk>[0-9]+)/$', views.PerfilDetail.as_view(), name=views.PerfilDetail.name),
    url(r'^obra/$', views.ObraList.as_view(), name=views.ObraList.name),
    url(r'^obra/(?P<pk>[0-9]+)/$', views.ObraDetail.as_view(), name=views.ObraDetail.name),
    url(r'^capitulo/$', views.CapituloList.as_view(), name=views.CapituloList.name),
    url(r'^capitulo/(?P<pk>[0-9]+)/$', views.CapituloDetail.as_view(), name=views.CapituloDetail.name),
    url(r'^pagina/$', views.PaginaDetail.as_view(), name=views.PaginaDetail.name),
    url(r'^pagina/(?P<pk>[0-9]+)/$', views.PaginaDetail.as_view(), name=views.PaginaDetail.name),
]