from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import logging
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

#imported models 
from .models import Set

# Create your views here.
def index(request):
    return render(request, 'cards/index.html')

def reports(request):
    return render(request, 'cards/reports.html')

@login_required 
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'http://127.0.0.1:8000'
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

def make_request(self, url, method="get", data=None, params=None):
    #LOGGER = logging.getLogger(__name__)
    #if type(data) == dict:
        #import json
        #data = json.dumps(data)

    if method == "get":
        tcg_response = requests.get("https://api.pokemontcg.io/v2/"+url)

    content = tcg_response.content.decode() if tcg_response.content else None
    return Response(content, status=tcg_response.status_code)

@api_view(['GET'])
def get_set(self):
    return make_request(self, "sets/swsh1", method="get")

@api_view(['GET'])
def get_card(self):
    return make_request(self, "cards?q=id:swsh1-1", method='get')