"""TestingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from api import views as api_views

router = DefaultRouter()
router.register('recipes',api_views.RecipeVersionViewSet)
router.register('users',api_views.UserViewSet, 'users')
router.register('recipes/(?P<recipe_pk>[^/.]+)/notes', api_views.NoteViewSet)
# router.register('recipes/(?P<recipe_pk>[^/.]+)/feedback', api_views.TasterFeedbackView)

#router.register('recipes/(?P<recipe_pk>[^/.]+)/notes/(?P<note_pk>[^/.]+)/feedback/(?P<feedback_pk>[^/.]+)', api_views.TasterFeedbackDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),

    # path('api/recipes/<int:recipe_pk>/tests/<int:note_pk>/feedback/', api_views.AnswerListCreateView.as_view(),    name="recipe_feedback",),
]
