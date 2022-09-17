from django.contrib import admin
from .models import User, Note, RecipeVersion

admin.site.register(User)
admin.site.register(Note)
admin.site.register(RecipeVersion)

