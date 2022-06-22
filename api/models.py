from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    


    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class RecipeVersion(models.Model):
    title = models.CharField(max_length=255)
    version_number = models.CharField(max_length=3)
    ingredients = models.TextField()
    recipe_steps = models.TextField()
    image = models.ImageField(blank=True, null=True)
    ready_for_feedback = models.BooleanField(default=False)
    successful_variation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='chefs', max_length=255) 
    base_recipe = models.ForeignKey('self', on_delete=models.CASCADE),
    # recipe_note_tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='tags', max_length=255)
    # recipe_note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='recipe_notes', max_length=255)
    
    #feedback_link = models.CharField(max_length=255, blank=True, null=True)
    # 2.0 - FK to TasterFeedback

    def __str__(self):
        return f"{self.title} by {self.chef}"


class Note(models.Model):
    note = models.TextField(blank=True, null=True)
    recipe_version = models.ForeignKey('RecipeVersion', on_delete=models.CASCADE, related_name='recipe_versions', max_length=255)


class Tag(models.Model):
    tag = models.CharField(max_length=255, blank=True, null=True)
    recipe_version_tag = models.ForeignKey('RecipeVersion', on_delete=models.CASCADE, related_name='recipe_version_tags', max_length=255, blank=True, null=True)
    note_tag = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='note_tags', max_length=255, blank=True, null=True)


class TasterFeedback(models.Model):
    ONE = '1' 
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

    RADIO = [ 
        (ONE , '1'), 
        (TWO , '2'), 
        (THREE , '3'), 
        (FOUR , '4'), 
        (FIVE , '5'), 
        ]

    TOO_LITTLE = 'Too Little'
    JUST_RIGHT = 'Just Right'
    TOO_MUCH = 'Too Much'

    SCALE = [ 
        (TOO_LITTLE , 'Too Little'), 
        (JUST_RIGHT , 'Just Right'),
        (TOO_MUCH , 'Too Much'), 
        ]
    
    YES = 'Yes'
    NO = 'No'

    CHOICE = [ 
        (YES , 'Yes'), 
        (NO , 'No'), 
        ]
    
    rating = models.CharField(max_length=6, choices=RADIO, default=THREE,)
    saltiness = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    sweetness = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    portion = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    texture = models.CharField(max_length= 5, choices=CHOICE, default=YES,)
    additional_comment = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    test_recipe = models.ForeignKey('RecipeVersion', on_delete=models.CASCADE, related_name='test_recipe', max_length = 255)
    test_version_number = models.ForeignKey('RecipeVersion', on_delete=models.CASCADE, related_name='test_version_number', max_length = 3)
    tester = models.ForeignKey('User', on_delete=models.CASCADE, related_name='taster', max_length=50)

    def __str__(self):
        return f"Feedback for {self.test_recipe}"