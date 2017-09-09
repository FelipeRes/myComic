from rest_framework import serializers
from core.models import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email','password')

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Perfil
		fields = ('url','username','resumo', 'born','cidade','pais', 'foto_perfil', 'obras')

class PerfilCreateSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		username = validated_data['usuario']['username']
		email = validated_data['usuario']['email']
		user = User.objects.create(username=username, email=email)
		user.set_password(validated_data['usuario']['password'])
		user.save()
		validated_data.pop('usuario')
		perfil = Perfil.objects.create(**validated_data)
		perfil.usuario = user
		perfil.save()
		return perfil
	foto_perfil = serializers.ImageField(max_length=None, allow_empty_file=True)
	usuario = UserSerializer()
	class Meta:
		model = Perfil
		fields = ('usuario','resumo', 'born','cidade','pais', 'foto_perfil',)

class ObraSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		obra = Obra.objects.create(**validated_data, publicacao=timezone.localdate(), status=Obra.PUBLICACAO, visualizacao=0, gostei=0)
		return obra
	capa = serializers.ImageField(max_length=None)
	class Meta:
		model = Obra
		fields = ('url','perfil','nome','sinopse','capa',)

class ObraDetailSerializer(serializers.HyperlinkedModelSerializer):
	capa = serializers.ImageField(max_length=None)
	publicacao = serializers.ReadOnlyField()
	status = serializers.ReadOnlyField()
	visualizacao = serializers.ReadOnlyField()
	gostei = serializers.ReadOnlyField()
	class Meta:
		model = Obra
		fields = ('url','perfil','nome','sinopse','publicacao','status','visualizacao','gostei','capa','capitulos')

class CapituloSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		obra = validated_data['obra']
		capitulo = Capitulo.objects.create(**validated_data, numero=obra.capitulos.count(), publicacao=timezone.localdate())
		return capitulo
	capa = serializers.ImageField(max_length=None)
	class Meta:
		model = Capitulo
		fields = ('obra','nome','capa',)

class PaginaSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		pagina = Pagina.objects.create(**validated_data, numero = validated_data['capitulo'].paginas.count() + 1)
		return pagina
	imagem = serializers.ImageField(max_length=None)
	class Meta:
		model = Pagina
		fields = ('url','capitulo','imagem',)

class CapituloDetailSerializer(serializers.HyperlinkedModelSerializer):
	capa = serializers.ImageField(max_length=None)
	paginas = PaginaSerializer(many=True)
	class Meta:
		model = Capitulo
		fields = ('url','obra','nome','numero','publicacao','capa','paginas')
	