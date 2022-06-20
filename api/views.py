from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from django.db.models import Count
from api.models import User, Recipe, Test
from rest_framework.viewsets import ModelViewSet
from api.serializers import TestSerializer, RecipeSerializer, UserCreateSerializer, UserSerializer


class UserViewSet(DjoserUserViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserCreateSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class



class RecipeViewSet(ModelViewSet):
    queryset          = Recipe.objects.all()
    serializer_class  = RecipeSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Recipe.objects.filter(title__icontains=self.request.query_params.get("search"))
        else:
            results = Recipe.objects.annotate(
                total_recipes=Count('recipe')
            )
        return results.order_by('-id')
# need to check line 22 for the future

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user  == instance.chef:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.chef:
            serializer.save()

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return RecipeSerializer
        return super().get_serializer_class()


class TestViewSet(ModelViewSet):
    queryset            = Test.objects.all().order_by('created_at')
    serializer_class    = TestSerializer
    #permission class for authenticated users?


    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

    def perform_destroy(self, instance):
        if self.request.user  == instance.chef:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.chef:
            serializer.save()