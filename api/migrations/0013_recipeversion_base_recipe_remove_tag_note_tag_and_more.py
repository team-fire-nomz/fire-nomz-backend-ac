# Generated by Django 4.0.5 on 2022-06-23 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_tasterfeedback_test_version_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeversion',
            name='base_recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.recipeversion'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='tag',
            name='note_tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='note_tag',
            field=models.ManyToManyField(related_name='tags', to='api.note'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='recipe_version_tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='recipe_version_tag',
            field=models.ManyToManyField(related_name='tags', to='api.recipeversion'),
        ),
    ]