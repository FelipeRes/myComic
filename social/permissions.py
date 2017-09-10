from rest_framework import permissions

class IsPostagemOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.usuario == request.user))

class IsCommentOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.usuario == request.user))

class IsMessageOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return (obj.perfil.usuario == request.user) or (obj.destino.usuario == request.user)

class IsUser(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.usuario == request.user))