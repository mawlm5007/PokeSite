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
    id = models.CharField(max_length=280),
    # percentage of this set completed, calculated by (totalCardOwned/totalCardSet)*100 
    percentCompleted = models.IntegerField(),
    # total cards in this specific set 
    totalCardSet = models.IntegerField(),
    # total cards the user owns in this set 
    totalCardOwned = models.IntegerField(), 
    # id of the user that this information relates to 
    user_id = ArrayField(models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),

    def __str__(self):
        return self.id


# card class 
class Card(models.Model):
    # id of the card 
    id = models.CharField(max_length=280),
    # boolean if we own the card or not 
    own = models.BooleanField(default=False),
    # the set that this card is apart of 
    set_id = ArrayField(models.ForeignKey(to=Set, on_delete=models.CASCADE)),

    def __str__(self):
        return self.id