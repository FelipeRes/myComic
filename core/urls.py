from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.conf import settings
from django.views.static import serve

from rest_framework.authtoken import views as rest_framework_views
from . import views as local_views

urlpatterns = [
    url(r'^perfil/$', views.PerfilList.as_view(), name=views.PerfilList.name),
    url(r'^perfil/create/$', views.PerfilCreate.as_view(), name=views.PerfilCreate.name),
    url(r'^perfil/(?P<pk>[0-9]+)/$', views.PerfilDetail.as_view(), name=views.PerfilDetail.name),
    url(r'^obra/$', views.ObraList.as_view(), name=views.ObraList.name),
    url(r'^obra/(?P<pk>[0-9]+)/$', views.ObraDetail.as_view(), name=views.ObraDetail.name),
    url(r'^obra/(?P<pk>[0-9]+)/capitulo/$', views.CapituloList.as_view(), name=views.CapituloList.name),
    url(r'^obra/(?P<pk>[0-9]+)/capitulo/create/$', views.CapituloCreate.as_view(), name=views.CapituloCreate.name),
    url(r'^capitulo/(?P<pk>[0-9]+)/$', views.CapituloDetail.as_view(), name=views.CapituloDetail.name),
    url(r'^pagina/(?P<pk>[0-9]+)$', views.PaginaDetail.as_view(), name=views.PaginaDetail.name),
    url(r'^capitulo/(?P<cap_pk>[0-9]+)/pagina/create$', views.PaginaCreate.as_view(), name=views.PaginaCreate.name),

    #url(r'^login/$', local_views.get_auth_token, name='login'),
    #url(r'^logout/$', local_views.logout_user, name='logout'),
    #url(r'^auth/$', local_views.login_form, name='login_form'),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]