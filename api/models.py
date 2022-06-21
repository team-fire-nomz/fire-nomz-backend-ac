from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    


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
        return f"{self.title} by {self.chef}"


class Test(models.Model):
    base_recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='tests', max_length = 255)
#temporarily set to charfield in order to research how to sequential number entries
    version_number = models.CharField(max_length=3)
    ingredients = models.TextField(max_length=500)
    recipe = models.TextField(max_length=800)  
    image = models.ImageField(blank=True, null=True)
    outside_notes = models.CharField(max_length=400, blank=True, null=True)
    final_notes = models.CharField(max_length=400, blank=True, null=True)
    adjustments = models.CharField(max_length=455, blank=True, null=True)
    feedback_link = models.URLField(max_length=255, )
#temporarily set to CharField, researching how to connect with tags component from react FE repo
    tags = models.CharField(max_length=255, blank=True, null=True)
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='test', max_length = 255)
    variation_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    successful_variation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.base_recipe}: Test #{self.version_number} "
