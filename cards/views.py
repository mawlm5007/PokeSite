from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

#imported models 
from .models import Set, Card

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


# rest functions 
def make_request(self, url, method="get", data=None, params=None):
    #LOGGER = logging.getLogger(__name__)
    #if type(data) == dict:
        #import json
        #data = json.dumps(data)

    if method == "get":
        tcg_response = requests.get("https://api.pokemontcg.io/v2/"+url)

    #print(type(tcg_response))
    content = tcg_response.content.decode() if tcg_response.content else None
    return HttpResponse(content, content_type='application/json')

@api_view(['GET'])
def get_set(self, id_set = "swsh1"):
    return make_request(self, "sets/"+id_set, method="get")

@api_view(['GET'])
def get_card(self, id_card = "swsh1-1"):
    return make_request(self, "cards?q=id:"+id_card, method='get')

# return https response 
#def get(self, request):
 #   id_card = "swsh1"
 #   response = get_set(id_card)
 #   return HttpResponse(response.data, content_type='application/json')

# create objects 
def create_set(self, id_set = "swsh1"):
    set_instance = Set()
    set_instance.set_id = id_set

    set_response = get_set(self, id_set)
    
    decoded_set_response = set_response.content
    json_response = json.loads(decoded_set_response)
    
    set_instance.totalCardSet = json_response['data']['total']
    #set_instance.totalCardOwned = 0
    #set_instance.user_id = request.user
    set_instance.save()
    return render(self, 'cards/index.html')

def create_card(request, id_card = 'swsh1-1'):
    card_instance = Card()
    card_instance.card_id = id_card
    card_instance.save()
    return render(request, 'cards/index.html')


