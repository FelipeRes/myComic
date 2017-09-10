from django.db import models
from core.models import Perfil
# Create your models here.

class Postagem(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='postagens')
	mensagem = models.CharField(max_length=1024)
	imagem = models.ImageField(upload_to = 'postagem/', default='postagem/None/no-img.jpg', blank=True, null=True)
	publicacao = models.DateTimeField()

	def __str__(self):
		return "Mensagem: " + self.mensagem + " Publicacao: " + str(self.publicacao)

class Comentario(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
	postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
	mensagem = models.CharField(max_length=1024)
	publicacao = models.DateTimeField()

class Mensagem(models.Model):
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_enviadas')
	destino = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='mensagens_recebidas')
	texto = models.CharField(max_length=1024)
	envio = models.DateTimeField()
	visualizada = models.BooleanField(default=False)
