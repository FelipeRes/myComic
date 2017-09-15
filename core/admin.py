from django.contrib import admin
from core.models import *
from social.models import *

# Register your models here.

admin.site.register(Obra)
admin.site.register(Capitulo)
admin.site.register(Pagina)
admin.site.register(Perfil)
admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(Mensagem)

