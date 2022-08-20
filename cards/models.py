from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

# set class 
class Set(models.Model):
    # id of the specific set 
    set_id = models.CharField(max_length=280, default="set")
    # percentage of this set completed, calculated by (totalCardOwned/totalCardSet)*100 
    percentCompleted = models.IntegerField(default=0)
    # total cards in this specific set 
    totalCardSet = models.IntegerField(default=0)
    # total cards the user owns in this set 
    totalCardOwned = models.IntegerField(default=0)
    # image of the set logo 
    set_logo = models.CharField(max_length=280, default="logo")
    # id of the user that this information relates to 
    user_id = models.ManyToManyField(to=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.set_id


# card class 
class Card(models.Model):
    # id of the card 
    card_id = models.CharField(max_length=280, default="card")
    # boolean if we own the card or not 
    own = models.BooleanField(default=False)
    # the set that this card is apart of 
    set_id = models.ManyToManyField(to=Set)
    # name of the card
    card_name = models.CharField(max_length=280, default="card")
    # small image of the card
    small_image = models.CharField(max_length=280, default="small")
    # big image of the card
    big_image = models.CharField(max_length=280, default="big")

    def __str__(self):
        return self.card_id