from rest_framework import serializers
from .models import Character, Campaign

class CharacterSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Character
        fields = ('name', 'race', 'subrace', 'class', 'background', 'skill proficiency')