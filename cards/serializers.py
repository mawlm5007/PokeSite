from rest_framework import serializers
from .models import Card, Set

class CardSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = ('card_id', 'own', 'set_id', 'card_name', 'small_image', 'big_image')

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set 
        fields = ('set_id', 'percentCompleted', 'totalCardSet', 'totalCardOwned', 'set_logo', 'user_id')
