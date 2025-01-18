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
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'rating', 'release_date', 'is_sponsored')
    list_filter = ('genre', 'rating', 'release_date', 'is_sponsored')
    search_fields = ('title', 'genre')
    ordering = ('-release_date',)

    actions = ['mark_as_sponsored']

    def mark_as_sponsored(self, request, queryset):
        queryset.update(is_sponsored=True)
    mark_as_sponsored.short_description = "Mark selected movies as sponsored"

admin.site.register(Movie, MovieAdmin)
