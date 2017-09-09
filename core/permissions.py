from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.usuario == request.user))

class IsObraOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.perfil.usuario == request.user))

class IsCapituloReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return ((request.method in permissions.SAFE_METHODS) or (obj.obra.perfil.usuario == request.user))