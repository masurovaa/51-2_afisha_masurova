from rest_framework import serializers
from .models import Film


class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        

class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = 'id name release_year'.split() # ['id', 'name']
        #fields = '__all__'
        #exclude = 'text is_active'.split()