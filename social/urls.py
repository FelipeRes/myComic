from django.conf.urls import url, include
from django.contrib import admin
from social import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^postagem/$', views.PostagemList.as_view(), name=views.PostagemList.name),
    url(r'^postagem/create/$', views.PostagemCreate.as_view(), name=views.PostagemCreate.name),
    url(r'^postagem/(?P<pk>[0-9]+)/$', views.PostagemDetail.as_view(), name=views.PostagemDetail.name),
    url(r'^comentario/$', views.ComentarioList.as_view(), name=views.ComentarioList.name),
    url(r'^comentario/(?P<pk>[0-9]+)/$', views.ComentarioDetail.as_view(), name=views.ComentarioDetail.name),
    url(r'^mensagem/$', views.MensagemList.as_view(), name=views.MensagemList.name),
    url(r'^mensagem/(?P<pk>[0-9]+)/$', views.MensagemDetail.as_view(), name=views.MensagemDetail.name),
    url(r'^seguir/$', views.SeguirView.as_view(), name=views.SeguirView.name),
    url(r'^deixar_seguir/$', views.DeixarSeguirView.as_view(), name=views.DeixarSeguirView.name),
    url(r'^timeline/$', views.TimeLine.as_view(), name=views.TimeLine.name),
]