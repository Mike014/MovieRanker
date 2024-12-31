# Recap: This file is used to define the URL patterns for the movie app.
# urlpatterns is a list of URL patterns that Django will use to match the requested URL to the appropriate view function.
# The path() function is used to define a URL pattern. It takes three arguments: the URL pattern, the view function to call, and an optional name for the URL pattern.
# Changes: 31/12/2024
# In this file, we define two URL patterns: one for the movie_list view and one for the movie_details view. 
# The movie_list URL pattern will match requests to /movies/ and call the movie_list view function. 
# The movie_details URL pattern will match requests to /movies/<movie_id>/ and call the movie_details view function, passing the movie_id as an argument.
from django.urls import path
from .views import movie_list, movie_details

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),  
    path('movies/<int:movie_id>/', movie_details, name='movie_details'),  
]