from rest_framework	import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "director", "actors", "year")

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id","name")