from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='perfil')
	resumo = models.TextField()
	born = models.DateField(null=True, blank=True)
	cidade = models.CharField(max_length=128, default='Não Informado')
	pais = models.CharField(max_length=128, default='Não Informado')
	foto_perfil = models.ImageField(upload_to = 'foto_perfil/', default = 'foto_perfil/None/no-img.jpg', blank=True, null=True)
	seguindo = models.ManyToManyField("self", blank=True, null=True, related_name='seguidores',symmetrical=False)

	@property
	def username(self):
		return self.usuario.username

	@property
	def email(self):
		return self.usuario.email

	@property
	def password(self):
		return self.usuario.password

	def __str__(self):
		return self.username + " - " + self.email

class Obra(models.Model):
	PUBLICACAO = 'P'
	FINALIZADO = 'F'
	STATUS_CHOICES = ((PUBLICACAO, 'Em publicação'),(FINALIZADO, 'Finalizado'))
	perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='obras')
	nome = models.CharField(max_length=128)
	sinopse = models.TextField()
	publicacao = models.DateField()
	status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PUBLICACAO)
	visualizacao = models.IntegerField()
	gostei = models.IntegerField()
	capa = models.ImageField(upload_to = 'obra_capa/', default = 'obra_capa/None/no-img.jpg')

	def __str__(self):
		return self.nome + " - " + self.sinopse

class Capitulo(models.Model):
	obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='capitulos')
	nome = models.CharField(max_length=128)
	numero = models.PositiveIntegerField()
	publicacao = models.DateField()
	capa = models.ImageField(upload_to = 'capitulo_capa/', default = 'capitulo_capa/None/no-img.jpg')
	
	def __str__(self):
		return "Nome:" + self.nome + " Numero: " + str(self.numero) + " Status: " + str(self.publicacao)

class Pagina(models.Model):
	capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE, related_name='paginas')
	numero = models.PositiveIntegerField()
	imagem = models.ImageField(upload_to = 'pagina/', default = 'pagina/None/no-img.jpg')
	def __str__(self):
		return "capitulo: " + self.capitulo.nome + " Pagina: " + str(self.numero)