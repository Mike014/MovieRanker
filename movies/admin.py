"""
This module registers the Movie model with the Django admin site.

Imports:
    admin (django.contrib.admin): The Django admin module.
    Movie (models.Movie): The Movie model from the current app's models.

Functionality:
    Registers the Movie model with the Django admin site to enable
    management of Movie instances through the admin interface.
"""

from django.contrib import admin

from .models import Movie

# Register your models here.
admin.site.register(Movie)
