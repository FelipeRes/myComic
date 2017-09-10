from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle
from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from core.models import *
from core.serializers import *
from django.contrib.auth import get_user_model
from core.permissions import *

class PerfilList(generics.ListAPIView):
	'''
    Retorna a lista de todos os perfils ativos
    '''
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer
	name ='perfil-list'	
	
class PerfilCreate(generics.CreateAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilCreateSerializer
	name ='perfil-create'	

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Perfil.objects.all()
	serializer_class = PerfilSerializer
	name ='perfil-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

	def delete(self, request, *args, **kwargs):
		user = request.user
		user.delete()
		return self.destroy(request, *args, **kwargs)

class ObraList(generics.ListCreateAPIView):
	queryset = Obra.objects.all()
	serializer_class = ObraSerializer
	name = 'obra-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsObraOrReadOnly)

class ObraDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Obra.objects.all()
	serializer_class = ObraDetailSerializer
	name = 'obra-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsObraOrReadOnly)
	def get_object(self):
		pk = self.kwargs.get('pk')
		obra = Obra.objects.get(pk=pk)
		print(obra)
		obra.visualizacao = obra.visualizacao+1
		obra.save()
		return super(ObraDetail, self).get_object()

class CapituloList(generics.CreateAPIView):
	queryset = Capitulo.objects.all()
	serializer_class = CapituloSerializer
	name = 'capitulo-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCapituloReadOnly)

class CapituloDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Capitulo.objects.all()
	serializer_class = CapituloDetailSerializer
	name = 'capitulo-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCapituloReadOnly)

class PaginaDetail(generics.CreateAPIView):
	queryset = Pagina.objects.all()
	serializer_class = PaginaSerializer
	name = 'pagina-detail'
