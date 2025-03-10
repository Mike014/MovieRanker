# Generated by Django 5.1.4 on 2025-01-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_movie_overview"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="affiliate_link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="movie",
            name="is_sponsored",
            field=models.BooleanField(default=False),
        ),
    ]
