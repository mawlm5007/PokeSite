from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
    path('getSet/', views.get_set, name='getSet'),
    path('getCard/', views.get_card, name='getCard'),
]