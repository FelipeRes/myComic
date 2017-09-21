from django.shortcuts import render, HttpResponse
import json
import httplib2
import urllib
from pprint import pprint
import requests
from django.conf import settings

# Create your views here.
headers = {'Content-type': "application/json"}
h = httplib2.Http()
def index(request):
	response, content = h.request(uri="http://localhost:8000/core/obra", method="GET", headers=headers)
	data = json.loads(content.decode())
	return render(request, 'index.html', data)

def obra(request, pk):
	response, content = h.request(uri="http://localhost:8000/core/obra/" + pk, method="GET", headers=headers)
	data = json.loads(content.decode())
	pprint(data)
	return render(request, 'obra.html', data)

def leitura(request, pk):
	response, content = h.request(uri="http://localhost:8000/core/capitulo/" + pk, method="GET", headers=headers)
	data = json.loads(content.decode())
	pprint(data)
	return render(request, 'leitura.html', data)

def minhas_obras(request, pk):
	response, content = h.request(uri="http://localhost:8000/core/perfil/" + pk + "/obra", method="GET", headers=headers)
	data = json.loads(content.decode())
	pprint(data)
	return render(request, 'minhas_obras.html', data)

def login(request):
	response, content = h.request(uri="http://localhost:8000/core/get_auth_token/", method="POST", headers=headers)
	pprint(content)
	data = json.loads(content.decode())
	pprint(data)
	return render(request, 'minhas_obras.html', data)