from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    recipe = models.TextField()
    ingredients = models.TextField()
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='chef', max_length=255) 
    recipe_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe} by {self.chef}"