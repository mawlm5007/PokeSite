from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
    path('getSet/', views.get_set, name='getSet'),
    path('getCard/', views.get_card, name='getCard'),
    path('createSet/', views.create_set, name='createSet'),
    path('createCard/', views.create_card, name='createCard'),
    path('populateSet/', views.populate_set, name='populateSet'),
    path('all_cards/', views.all_cards, name='all_cards')
]