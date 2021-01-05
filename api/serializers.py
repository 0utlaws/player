from rest_framework import serializers

from movies import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description', 'movies_amount']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ['id', 'name', 'surname', 'birth_place', 'show_pictures']


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = ['id', 'actor', 'image']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'file', 'title', 'description', 'category', 'actors']


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Access
        fields = ['id', 'movie', 'user', 'has_access']