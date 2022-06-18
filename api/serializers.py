from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField(read_only=True,)

    class Meta:
        model  = Recipe
        fields = [
            'id',
            'title',
            'recipe',
            'chef',
            'created_at',
            ]