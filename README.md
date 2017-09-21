# myComic
Rede social para autores de quadrinhos independentes. O sistema se trata de uma API Rest desenvolvida com *django rest framework* onde o usuário pode tanto visualizar como criar obras de história em quadrinhos.
O cliente da API se encontra na pasta *my_comic_cliente*
 ## Entidades e diagrama entidade-relacionamento:
 O sistema apresenta 2 módulos: Criação(core) e social.
 ![alt text](https://github.com/FelipeRes/myComic/blob/master/docs/imagem.png)
 
 ## Autenticação:
 
 A autenticação do sistema funciona por token, utilizando o *rest_framework.authtoken*. Qunado o usuario cria um perfil, um token é gerado automaticamente para ele no banco de dados.
 O token é obtido através de um post para a url *core/get_auth_token/*. Esse post deve conter um JSON com "username" e "password".
 A aplicação cliente faz a requisição via *axios* e guarda o token na memoria do navegador:
 ```javascript
 # no cliente /core/templates/base.html
 axios.post('http://localhost:8000/core/get_auth_token/', crendentials)
	.then(function(response){
		localStorage.setItem('token',response.data.token)
		menu.logged = true
		Materialize.toast('Olá ' + login.crendentials.username, 3000, 'rounded')
	})
		.catch(e => {
		console.log(e)
	})
 ```
 
 ## Permissão:
 Os usuarios tem permissão para visualizar todo tipo de coisa, mas só possuem permissão para criar objetos casos estenjam autenticados via token.
 Os usuarios também só podem aleterar obras, capitulos, paginas e posts que eles mesmos tenham criado. Eles também só podem adicionar capítulos e páginas em obras da qual eles sejam proprietários.
 Exemplo:
  ```python
  #no servidor /core/permissions.py
  class IsPaginaCreateOrReadOnly(permissions.BasePermission):
	def has_object_permission(sefl, request, view, obj):
		capitulo_id = request.resolver_match.kwargs.get('pk') 
		capitulo = Capitulo.objects.get(pk=capitulo_id)
		if capitulo.criado_por.user == request.user:
			return True
		else:
			return False
 ``` 
 Esta formaliza um permissão que restringe o usuario a adicionar páginas apenas para capitulos da qual ele seja proprietário.
 A única rota disponível para ciração de páginas exige o id do capítulo para qual a pagina se destina. Com esse id é possível resgatar o capitulo e checar se ele pertence ao usuario que está fazendo a requisição.
  ```python
 #no servidor /core/urls.py
 url(r'^capitulo/(?P<pk>[0-9]+)/pagina/create$', views.PaginaCreate.as_view(), name=views.PaginaCreate.name),
 ```
 
 ## [Swagger](https://github.com/marcgibbons/django-rest-swagger):
 Swagger é uma framework que gera a documentação da API Rest do sistema.
 ```python
  INSTALLED_APPS = (
        ...
        'rest_framework_swagger',
    )
```
A sua rota está localizada no endpoint do sistema.
 ```python
#no servidor /core/urls.py
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view),
    ...
```
![alt text](https://github.com/FelipeRes/myComic/blob/master/docs/documentacao.png)
 ## Throttling:
O sistema não permite quantidades ilimitadas de requisição, para isso utiliza as classes *rest_framework.throttling.AnonRateThrottle* e *rest_framework.throttling.UserRateThrottle*. Ele limita o uso para usuarios anônimos em 1000 requisições por hora e 10000 requisições por hora para usuários não atenticados.
 ```python
 #no servidor /MyComic/settings.py
 'DEFAULT_THROTTLE_RATES':{
        'anon':'1000/hour',
        'user': '10000/hour',
    },
 ```
