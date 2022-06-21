from django.contrib import admin
from .models import User, Test, RecipeVersion, TasterFeedback

admin.site.register(User)
admin.site.register(Test)
admin.site.register(RecipeVersion)
admin.site.register(TasterFeedback)
