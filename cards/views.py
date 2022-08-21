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
from .models import Set, Card, User

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


# rest class
class TCG_API():
    __instance = None 
    user_id = None

    @staticmethod
    def getInstance():
        """ Static access method """
        if TCG_API.__instance == None:
            TCG_API()
        return TCG_API.__instance
    
    def __init__(self):
        """ Virtually private constructor """
        if TCG_API.__instance != None:
            raise Exception("This class is a singleton")
        else:
            TCG_API.__instance = self




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
def create_set(self, id_set = "swsh2"):
    set_instance = Set()
    set_instance.set_id = id_set

    set_response = get_set(self, id_set)
    
    decoded_set_response = set_response.content
    json_response = json.loads(decoded_set_response)
    
    set_instance.totalCardSet = json_response['data']['total']
    
    set_instance.set_logo = json_response['data']['images']['logo']
    #set_instance.totalCardOwned = 0   
    set_instance.save()

    set_instance.user_id.add(self.user)
    #set_instance.user_id = self.user.id
    return set_instance
    #return render(self, 'cards/index.html')

def create_card(request, id_card = 'swsh1-220', set = Set()):
    card_instance = Card()
    card_instance.card_id = id_card
    
    card_response = get_card(request, id_card)

    decoded_card_response = card_response.content
    json_response = json.loads(decoded_card_response)

    # check to see if the card exists 
    if not json_response['data']:
        return 0

    card_instance.card_name = json_response['data'][0]['name']

    card_instance.big_image = json_response['data'][0]['images']['large']

    card_instance.small_image = json_response['data'][0]['images']['small']

    card_instance.save()

    card_instance.set_id.add(set)

    return card_instance
    #return render(request, 'cards/index.html')


# function to add all cards in a set for a user 
def populate_set(self, id_set = 'swsh9'):
    
    # we create the set instance 
    set_instance = create_set(self, id_set)
    
    # loop create_card while card_number <= set_instance.totalCardSet
    card_number = 1
    while (card_number <= set_instance.totalCardSet):
        id_card = set_instance.set_id + "-" + str(card_number)
        
        create_card(self, id_card, set_instance)
        card_number = card_number + 1

    return render(self, 'cards/index.html')
    
def all_cards(request):
    card_list = Card.objects.all()
    return render(request, 'cards/reports.html', 
    {'card_list': card_list})