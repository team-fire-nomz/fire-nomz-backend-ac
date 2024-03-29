from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from django.db.models import Count
from requests import Response
from rest_framework.generics import get_object_or_404
from api.models import User, RecipeVersion, Note
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import NoteSerializer, RecipeVersionSerializer, UserCreateSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsChefOrReadOnly, RecipeIsChefOrReadOnly
from django.db.models import Q


class UserViewSet(DjoserUserViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserCreateSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class


class RecipeVersionViewSet(ModelViewSet):
    queryset          = RecipeVersion.objects.all()
    serializer_class  = RecipeVersionSerializer
    permission_classes = (RecipeIsChefOrReadOnly,)

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = RecipeVersion.objects.filter(
                Q(title__icontains=search_term) |
                Q(ingredients__icontains=search_term)
            )
            results.order_by('-id')

        else:
            results = RecipeVersion.objects.annotate(
                total_recipes=Count('recipe_steps')
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
            return RecipeVersionSerializer
        return super().get_serializer_class()


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsChefOrReadOnly]

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Note.objects.filter(
                Q(note__icontains=search_term)
                )
            results

        else:
            results = Note.objects.annotate(
                total_recipes=Count('note')
            )
        return results.order_by('-id')

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(note_by=self.request.user)

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.note_by:
            serializer.save()
