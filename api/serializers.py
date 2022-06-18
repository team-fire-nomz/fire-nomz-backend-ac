from rest_framework import serializers
from .models import User, Recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )

class RecipeSerializer(serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model  = Recipe
        fields = [
            'id',
            'title',
            'ingredients',
            'recipe',
            'chef',
            'created_at',
            ]