"""
This module defines the URL patterns for the Movies app.

Imports:
    path (django.urls.path): A function to define URL patterns.
    movie_details (movies.views.movie_details): The view function to display movie details.
    movie_list (movies.views.movie_list): The view function to display a list of movies.

URL Patterns:
    urlpatterns (list): A list of URL patterns that Django will use to match the requested URL to the appropriate view function.
        - "" (home): Matches the root URL and calls the movie_list view function.
        - "movies/" (movie_list): Matches the URL /movies/ and calls the movie_list view function.
        - "movies/<int:movie_id>/" (movie_details): Matches the URL /movies/<movie_id>/ and calls the movie_details view function, passing the movie_id as an argument.
"""

from django.urls import path

from .views import movie_details, movie_list

urlpatterns = [
    path("", movie_list, name="home"),
    path("movies/", movie_list, name="movie_list"),
    path("movies/<int:movie_id>/", movie_details, name="movie_details"),
]
