from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class Test(models.Model):
    title = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='chef', max_length = 255)
#temporarily set to charfield in order to research how to sequential number entries
    version_number = models.CharField(max_length=3)
    ingredients = models.TextField(max_length=500)
    recipe = models.TextField(max_length=800)  
    image = models.ImageField()
    outside_notes = models.CharField(max_length=400)
    final_notes = models.CharField(max_length=400)
    adjustments = models.CharField(max_length=455)
    feedback_link = models.URLField(max_length=255)
#temporarily set to CharField, researching how to connect with tags component from react FE repo
    tags = models.CharField(max_length=255)
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='chef', max_length = 255)
    variation_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    successful_variation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.chef}"


class Recipe(models.Model):
    pass