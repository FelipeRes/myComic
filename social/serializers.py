from rest_framework import serializers
from social.models import *
from django.utils import timezone

class ComentarioSerializer(serializers.ModelSerializer):
	def create(self, validate_data):
		comentario = Comentario.objects.create(**validate_data, publicacao=timezone.localdate())
		return comentario
	class Meta:
		model = Comentario
		fields = ('perfil', 'postagem', 'mensagem',)

class ComentarioDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Comentario
		fields = ('perfil', 'postagem', 'mensagem', 'publicacao',)

class PostagemSerializer(serializers.ModelSerializer):
	def create(self, validate_data):
		postagem = Postagem.objects.create(**validate_data, publicacao=timezone.localdate())
		return postagem
	imagem = serializers.ImageField(max_length=None,allow_empty_file=True,required=False)
	class Meta:
		model = Postagem
		fields = ('perfil', 'mensagem', 'imagem',)

class PostagemDetailSerializer(serializers.HyperlinkedModelSerializer):
	publicacao = serializers.ReadOnlyField()
	imagem = serializers.ImageField(max_length=None,allow_empty_file=True,required=False)
	comentarios = ComentarioDetailSerializer(many=True)
	class Meta:
		model = Postagem
		fields = ('url', 'perfil', 'mensagem', 'imagem', 'publicacao', 'comentarios',)

class MensagemSerializer(serializers.HyperlinkedModelSerializer):
	def create(self, validate_data):
		mensagem = Mensagem.objects.create(**validate_data, visualizada=False, envio=timezone.now())
		return mensagem
	class Meta:
		model = Mensagem
		fields = ('url', 'perfil', 'destino', 'texto',)

class MensagemDetailSerializer(serializers.HyperlinkedModelSerializer):
	visualizada = serializers.ReadOnlyField()
	envio = serializers.ReadOnlyField()
	class Meta:
		model = Mensagem
		fields = ('url', 'perfil', 'destino', 'texto', 'envio', 'visualizada',)