from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('characters/', views.Characters.as_view(), name="characters"),
    path('characters/creator/', views.CharacterCreator.as_view(), name="character_creator"),
    path('characters/<int:pk>', views.CharacterDetail.as_view(), name="character_detail")

]