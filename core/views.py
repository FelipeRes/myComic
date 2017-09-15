from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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
	def perform_create(self, serializers):
		serializers.save(perfil=self.request.user.perfil)

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

class CapituloList(generics.ListAPIView):
	serializer_class = CapituloDetailSerializer
	name = 'capitulo-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCapituloReadOnly)
	def get_queryset(self):
		obra = Obra.objects.get(pk=self.kwargs['pk'])
		return Capitulo.objects.filter(obra=obra)

class CapituloCreate(generics.ListCreateAPIView):
	serializer_class = CapituloSerializer
	name = 'capitulo-create'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCapituloReadOnly)
	def get_queryset(self):
		obra = Obra.objects.get(pk=self.kwargs['pk'])
		return Capitulo.objects.filter(obra=obra)
	def perform_create(self, serializers):
		obra = Obra.objects.get(pk=self.kwargs['pk'])
		obras = self.request.user.perfil.obras.all()
		if obra in obras:
			serializers.save(obra=obra)
		else:
			raise ValidationError('You have not have permission')

class CapituloDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Capitulo.objects.all()
	serializer_class = CapituloDetailSerializer
	name = 'capitulo-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCapituloReadOnly)

class PaginaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pagina.objects.all()
	serializer_class = PaginaDetailSerializer
	name = 'pagina-detail'

class PaginaCreate(generics.CreateAPIView):
	queryset = Pagina.objects.all()
	serializer_class = PaginaSerializer
	name = 'pagina-create'
	def perform_create(self, serializers):
		capitulo = Capitulo.objects.get(pk=self.kwargs['cap_pk'])
		print(1)
		if capitulo.obra.perfil == self.request.user.perfil:
			print(2)
			numero = capitulo.paginas.count() + 1
			serializers.save(capitulo=capitulo, numero = numero)
		else:
			raise ValidationError('You have not have permission')

