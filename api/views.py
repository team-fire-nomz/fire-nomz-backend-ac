from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from django.db.models import Count
from rest_framework.generics import get_object_or_404
from api.models import User, Recipe, Test, TasterFeedback
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import TestSerializer, RecipeSerializer, UserCreateSerializer, UserSerializer, TasterFeedbackSerializer, TasterFeedbackDetailSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(DjoserUserViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = UserCreateSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class


class RecipeViewSet(ModelViewSet):
    queryset          = Recipe.objects.all()
    serializer_class  = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Test.objects.filter(base_recipe_id=self.kwargs["recipe_pk"])

    def perform_create(self, serializer, **kwargs):
        base_recipe = get_object_or_404(Recipe, pk=self.kwargs["recipe_pk"])
        serializer.save(chef=self.request.user, base_recipe=base_recipe)

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.chef:
            serializer.save()


class TasterFeedbackView(ModelViewSet):
    queryset = TasterFeedback.objects.all().order_by('created_at')
    serializer_class = TasterFeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        test_version_number = get_object_or_404(Test, pk=self.kwargs["test_pk"])
        test_recipe = get_object_or_404(Test, pk=self.kwargs["test_pk"])
        if self.request.user.is_authenticated:
            serializer.save(tester=self.request.user, test_version_number=test_version_number, test_recipe=test_recipe)

    def perform_destroy(self, instance):
        if self.request.user  == instance.tester:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.tester:
            serializer.save()


class TasterFeedbackDetailView(ModelViewSet):
    queryset = TasterFeedback.objects.all().order_by('created_at')
    serializer_class = TasterFeedbackDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self): 
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def perform_destroy(self, instance):
        if self.request.user  == instance.tester:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.tester:
            serializer.save()