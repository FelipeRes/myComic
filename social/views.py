from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from social.models import *
from social.serializers import *
from social.permissions import *
from django.contrib.auth import get_user_model


User = get_user_model()

class PostagemCreate(generics.CreateAPIView):
	queryset = Postagem.objects.all()
	serializer_class = PostagemSerializer
	name = 'postagem-create'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsPostagemOrReadOnly)

class PostagemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Postagem.objects.all()
	serializer_class = PostagemSerializer
	name = 'postagem-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsPostagemOrReadOnly)

class PostagemList(generics.ListAPIView):
	queryset = Postagem.objects.all()
	serializer_class = PostagemDetailSerializer
	name = 'postagem-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsPostagemOrReadOnly)

class ComentarioList(generics.CreateAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer
	name ='comentario-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOrReadOnly)

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioDetailSerializer
	name ='comentario-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCommentOrReadOnly)

class MensagemList(generics.ListCreateAPIView):
	queryset = Mensagem.objects.all()
	serializer_class = MensagemSerializer
	name ='mensagem-list'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMessageOrReadOnly)

class MensagemDetail(generics.RetrieveUpdateDestroyAPIView):
	def get_object(self):
		pk = self.kwargs.get('pk')
		mensagem = Mensagem.objects.get(pk=pk)
		mensagem.visualizada = True
		mensagem.save()
		return super(MensagemDetail, self).get_object()
	queryset = Mensagem.objects.all()
	serializer_class = MensagemDetailSerializer
	name ='mensagem-detail'
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsMessageOrReadOnly)

class SeguirView(APIView):
	permission_classes = (IsAuthenticated,)
	name = 'seguir'
	def post(self, request, format=None):
		if not Perfil.objects.filter(id=request.data['perfil_id']).exists():
			content = {
				"mensagem": "perfil não existe"
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		perfil = Perfil.objects.get(id=request.data['perfil_id'])
		if not request.user.perfil in perfil.seguidores.all():
			perfil.seguidores.add(request.user.perfil)
			content = {
				"mensagem": "perfil "+ request.user.username + " está seguindo " + perfil.username
			}
			return Response(content, status=status.HTTP_202_ACCEPTED)
		else:
			content = {
				"mensagem": "perfil "+ request.user.username + " já está seguindo " + perfil.username
			}
			return Response(content, status=status.HTTP_202_ACCEPTED)

class DeixarSeguirView(APIView):
	permission_classes = (IsAuthenticated,)
	name = 'deixar-seguir'
	def post(self, request, format=None):
		if not Perfil.objects.filter(id=request.data['perfil_id']).exists():
			content = {
				"mensagem": "perfil não existe"
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)
		perfil = Perfil.objects.get(id=request.data['perfil_id'])
		
		if request.user.perfil in perfil.seguidores.all():
			perfil.seguidores.remove(request.user.perfil)
			content = {
				"mensagem": "perfil "+ request.user.username + " deixou de seguir " + perfil.username
			}
			return Response(content, status=status.HTTP_202_ACCEPTED)
		else:
			content = {
				"mensagem": "perfil "+ request.user.username + " nunca seguiu " + perfil.username
			}
			return Response(content, status=status.HTTP_202_ACCEPTED)