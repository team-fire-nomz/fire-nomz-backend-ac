from django.shortcuts import render
from django.db.models import Count
from api.models import Recipe
from rest_framework.viewsets import ModelViewSet
from api.serializers import RecipeSerializer


class RecipeViewSet(ModelViewSet):
    queryset          = Recipe.objects.all()
    serializer_class  = RecipeSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Recipe.objects.filter(title__icontains=self.request.query_params.get("search"))
        else:
            results = Recipe.objects.annotate(
                total_answers=Count('tests')
            )
        return results

    def perform_destroy(self, instance):
        if self.request.user  == instance.creator:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.creator:
            serializer.save()
