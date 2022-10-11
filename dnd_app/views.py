from urllib import request
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from dnd_app.models import Character
from django.forms import modelformset_factory
from django.views.generic.edit import CreateView
from django import forms
# from extra_views import Model
# Create your views  here.

class Home(TemplateView):
    template_name = "home.html"

class Characters(TemplateView):
    template_name = "characters.html"

class CharacterCreator(CreateView):
    model = Character
    fields = '__all__'
    template_name = "character_creator.html"
    success_url = "/characters/"

# def character_creator(request):
#     CharacterFormSet = modelformset_factory(Character, fields=('__all__'))
#     if request.method == 'POST':
#         formset = CharacterFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#     else:
#         formset = CharacterFormSet() 
#         form = CharacterForm()
#     return render(request, 'character_creator.html', {'formset': formset}, {'form': form})

# class CharacterCreator(forms.Form):
#     model = Character
#     race = forms.Select
#     background = forms.CheckboxSelectMultiple


# def character_creator(request):
#     context = {}
#     form = CharacterForm(request.POST or None, request.Files or None)
#     if form.is_valid():
#         form.save()
#     else:
#         form = CharacterForm()
#     context['form'] = form
#     return render(request, 'home.html', context)
