from rest_framework import permissions


class IsChefOrReadOnly(permissions.BasePermission):
    message = 'Editing posts is restricted to the chef only.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.recipe_version.chef == request.user:
            return True
        return False