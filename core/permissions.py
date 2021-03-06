from rest_framework import permissions
from core.models import *

class IsUserOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.usuario == request.user))

class IsObraOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		print('CHEGOU NA PERMISSÂO')
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.usuario == request.user))

class IsCapituloReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.obra.perfil.usuario == request.user))

class IsCapituloCreateOrReadOnly(permissions.BasePermission):
	def has_permission(sefl, request, view, obj):
		obra_id = request.resolver_match.kwargs.get('pk') 
		obra = Obra.objects.get(pk=obra_id)
		if obra.perfil.user == request.user:
			return True
		else:
			return False

class IsPaginaCreateOrReadOnly(permissions.BasePermission):
	def has_object_permission(sefl, request, view, obj):
		capitulo_id = request.resolver_match.kwargs.get('pk') 
		capitulo = Capitulo.objects.get(pk=capitulo_id)
		if capitulo.criado_por.user == request.user:
			return True
		else:
			return False