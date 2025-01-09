"""
This module defines the URL patterns for the Movies app.

Imports:
    path (django.urls.path): A function to define URL patterns.
    views (movies.views): The views module containing view functions for the Movies app.

URL Patterns:
    urlpatterns (list): A list of URL patterns that Django will use to match the requested URL to the appropriate view function.
        - "" (home): Matches the root URL and calls the home_view function.
        - "movies/" (movie_list): Matches the URL /movies/ and calls the movie_list function.
        - "profile/" (user_profile): Matches the URL /profile/ and calls the user_profile function.
        - "subscribe/" (subscribe): Matches the URL /subscribe/ and calls the subscribe function.
        - "movies/<int:movie_id>/" (movie_details): Matches the URL /movies/<movie_id>/ and calls the movie_details function, passing the movie_id as an argument.
"""

from django.urls import path

from . import views

urlpatterns = []

# Check if the views exist before adding them to urlpatterns
if hasattr(views, "home_view"):
    urlpatterns.append(path("", views.home_view, name="home"))
else:
    print("Warning: 'home_view' does not exist in views.")

if hasattr(views, "movie_list"):
    urlpatterns.append(path("movies/", views.movie_list, name="movie_list"))
else:
    print("Warning: 'movie_list' does not exist in views.")

if hasattr(views, "user_profile"):
    urlpatterns.append(path("profile/", views.user_profile, name="user_profile"))
else:
    print("Warning: 'user_profile' does not exist in views.")

if hasattr(views, "subscribe"):
    urlpatterns.append(path("subscribe/", views.subscribe, name="subscribe"))
else:
    print("Warning: 'subscribe' does not exist in views.")

if hasattr(views, "movie_details"):
    urlpatterns.append(
        path("movies/<int:movie_id>/", views.movie_details, name="movie_details")
    )
else:
    print("Warning: 'movie_details' does not exist in views.")
