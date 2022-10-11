from urllib import request
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from dnd_app.models import Character
from django.forms import modelformset_factory
from django.views.generic.edit import CreateView
from django import forms
from django.views.generic import DetailView
# from extra_views import Model
# Create your views  here.

class Home(TemplateView):
    template_name = "home.html"

class Characters(TemplateView):
    template_name = "characters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = Character.objects.all()
        return context

class CharacterCreator(CreateView):
    model = Character
    fields = ['name', 'race', 'subrace', 'class', 'background', 'skillProficiency', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    template_name = "character_creator.html"
    success_url = "/characters/"

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

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
