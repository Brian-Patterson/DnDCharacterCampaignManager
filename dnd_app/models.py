from cProfile import label
from random import choices
from django.db import models
from django.forms import ModelForm
from django import forms
from .choices import *

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=100, choices=RACE_CHOICES, null=True)
    subrace = models.CharField(max_length=100, choices=SUBRACE_CHOICES, null=True)
    job = models.CharField(max_length=100, choices=CLASS_CHOICES, name='class', null=True)
    background = models.CharField(max_length=100, choices=BACKGROUND_CHOICES)
    skillProficiency = models.CharField(max_length=100, choices=SKILL_PROFICIENCY_CHOICES)
    strength = models.SmallIntegerField(null=True)
    dexterity = models.SmallIntegerField(null=True)
    constitution = models.SmallIntegerField(null=True)
    intelligence = models.SmallIntegerField(null=True)
    wisdom = models.SmallIntegerField(null=True)
    charisma = models.SmallIntegerField(null=True)
    hitPoints = models.SmallIntegerField(null=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    schedule = models.DateTimeField(max_length=100)
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES)
    currentNumber = models.SmallIntegerField(null=True)
    neededNumber = models.SmallIntegerField(null=True)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    details = models.TextField(max_length=500)

