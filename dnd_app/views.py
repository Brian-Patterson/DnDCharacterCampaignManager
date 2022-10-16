from dataclasses import dataclass
from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import TemplateView
from dnd_app.models import Campaign, Character
from django.forms import modelformset_factory
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json, requests, asyncio
from .serializers import CharacterSerializer


# from extra_views import Model
# Create your views  here.
def api(request):

    # url = f"https://www.dnd5eapi.co/api/classes/"
    # response = requests.get(url)
    # data = response.json()
    # print(data)
    # spelled = []
    # spell = data
    # spelled.append(spell)
    url = f"https://www.dnd5eapi.co/api/classes/"
    response = requests.get(url)
    data = response.json()
    print(data)
    spelled = []
    for i in range(data['count']):
        spell = data['results'][i]['url']
        spelled.append(spell)
    
    
    filled = []
    for i in range(data['count']):
        source = f"https://www.dnd5eapi.co{spelled[i]}"
        response = requests.get(source)
        dottie = response.json()
        filled.append(dottie)


    context = {
        'data':data,
        'spell_loop': range(data['count']),
        'spelled': spelled,
        'filled': filled,


    }
    return render(request, 'api.html', context)


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.filter(user=self.request.user)
            context["header"] = "Your Characters"
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["campaigns"] = Campaign.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class Characters(TemplateView):
    template_name = "characters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.filter(user=self.request.user)
            context["header"] = "Your Characters"
        return context

@method_decorator(login_required, name='dispatch')
class Campaigns(TemplateView):
    template_name = "campaigns.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["campaigns"] = Campaign.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["campaigns"] = Campaign.objects.filter(user=self.request.user)
            context["header"] = "Your Campaigns"
        return context

class CharacterCreator(CreateView):
    model = Character
    fields = ['name', 'race', 'subrace', 'class', 'background', 'skillProficiency', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    template_name = "character_creator.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreator, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('character_detail', kwargs={'pk': self.object.pk})
    def form_choice(request):
        
        race_id = request.GET.get('race')
        subrace = Race.objects.filter(race_id=race_id)
        return render(request, 'dropdown_subraces.html', {'subrace': subrace})


class CampgaignCreator(CreateView):
    model = Campaign
    fields = ['title', 'schedule', 'frequency', 'currentNumber', 'neededNumber', 'location', 'details']
    template_name = "campaign_creator.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CampgaignCreator, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('campaigns_detail', kwargs={'pk': self.object.pk})


class CharacterDetail(DetailView):
    model = Character
    template_name = "character_details.html"

class CampgainDetail(DetailView):
    model = Campaign
    template_name = "campaign_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name, user=self.request.user)
            context["campaigns"] = Campaign.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.filter(user=self.request.user)
            context["campaigns"] = Campaign.objects.filter(user=self.request.user)
            context["header"] = "Your Campaigns"
        return context

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'race', 'subrace', 'class', 'background', 'skillProficiency', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    template_name = 'character_update.html'
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CampaignUpdate(UpdateView):
    model = Campaign
    fields = ['title', 'schedule', 'frequency', 'currentNumber', 'neededNumber', 'location', 'details']
    template_name = 'campaign_update.html'
    def get_success_url(self):
        return reverse('campaigns_detail', kwargs={'pk': self.object.pk})
    

class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"

class CampaignDelete(DeleteView):
    model = Campaign
    template_name = "campaign_delete.html"
    success_url = "/campaigns/"

class CampaignCharacterAssoc(View):
    def get(self, request, pk, character_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Campaign.objects.get(pk=pk).characters.remove(character_pk)
        if assoc == "add":
            Campaign.objects.get(pk=pk).characters.add(character_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context ={"form": form}
        return render(request, "registration/signup.html", context)
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else: 
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class NewsDataView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news_data = requests.get(
            'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ece95912ea3746e68826c8eb30e2eb66')
        context['newsdata'] = json.dumps(news_data.json(),
                                         sort_keys=True,
                                         indent=4)
        return context

def home(request):
    response = requests.get('https://www.dnd5eapi.co/api/')
    response.text
    print(response)
    return render(request, 'home.html', {
        print(response.text)
    })

def load_subraces(request):
    race_id = request.GET.get('race')
    subrace = Race.objects.filter(race_id=race_id)
    return render(request, 'dropdown_subraces.html', {'subrace': subrace})

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

