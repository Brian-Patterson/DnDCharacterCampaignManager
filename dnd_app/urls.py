from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('characters/', views.Characters.as_view(), name="characters"),
    path('characters/creator/', views.CharacterCreator.as_view(), name="character_creator"),
    path('characters/<int:pk>', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name="character_delete"),
    path('campaigns/', views.Campaigns.as_view(), name="campaigns"),
    path('campaigns/<int:pk>', views.CampgainDetail.as_view(), name="campaigns_detail"),
    path('campaigns/creator', views.CampgaignCreator.as_view(), name="campaign_creator"),
    path('campaigns/<int:pk>/update', views.CampaignUpdate.as_view(), name="campaign_update"),
    path('campaigns/<int:pk>/delete', views.CampaignDelete.as_view(), name="campaign_delete"),
    path('campaigns/<int:pk>/characters/<int:character_pk>/', views.CampaignCharacterAssoc.as_view(), name="campaign_character_assoc"),

]