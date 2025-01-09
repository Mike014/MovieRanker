"""
This module defines the Movie model for the Movies app.

Imports:
    models (django.db.models): The Django models module.
"""

from django.db import models


class Movie(models.Model):
    """
    This class represents a movie with its details.

    Attributes:
        title (str): The title of the movie.
        genre (str): The genre of the movie.
        rating (float): The rating of the movie.
        overview (str): A brief overview of the movie.
        release_date (date): The release date of the movie.
    """

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    overview = models.TextField(default="")
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the Movie instance, which is its title.
        """
        return self.title
