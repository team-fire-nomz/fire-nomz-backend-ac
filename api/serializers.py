from dataclasses import fields
from turtle import title
from rest_framework import serializers
from .models import Test, User, Recipe

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

class TestSerializer(serializers.ModelSerializer):
    #might change to Name once User model is discussed futher
    chef        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    title       = serializers.SlugRelatedField(read_only=True, slug_field="title")
    class Meta:
        model  = Test
        fields = [
            'id',
            'title',
            'version_number',
            'ingredients',
            'recipe',
            'image',
            'outside_notes',
            'final_notes',
            'adjustments',
            'feedback_link',
            'tags',
            'chef',
            'variation_complete',
            'created_at',
            'successful_variation',
        ]