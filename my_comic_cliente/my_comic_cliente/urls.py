"""my_comic_cliente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index, name='index'),
    url(r'^obra/(?P<pk>[0-9]+)/$', views.obra, name='obra'),
    url(r'^leitura/(?P<pk>[0-9]+)/$', views.leitura, name='leitura'),
    url(r'^minhas_obras/(?P<pk>[0-9]+)/$', views.minhas_obras, name='minhas_obras'),
    url(r'^login/$', views.login, name='login')
]
