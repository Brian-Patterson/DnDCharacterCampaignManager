from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('bnb/characters/', views.Characters.as_view(), name="characters"),
    path('bnb/characters/creator/', views.CharacterCreator.as_view(), name="character_creator"),


]