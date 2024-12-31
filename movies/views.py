# Recap: This file is used to define the views for the movie app.
# The views in this file are used to display the list of movies by genre and the details of a specific movie.
# The movie_list view is used to display the list of movies by genre. It takes the request as an argument.
# The movie_details view is used to display the details of a specific movie. It takes the request and movie_id as arguments.
# Changes: 31/12/2024
# In this file, we define two views: one to display the list of movies by genre and one to display the details of a specific movie.
# The movie_list view will render the movie_list.html template with the list of movies and genres.
# The movie_details view will render the movie_details.html template with the details of a specific movie.

from django.shortcuts import render
from .api import get_movie_lists, get_genre_lists, get_movie_details
from .models import Movie

def movie_list(request):
    """
    View to display movies by genre and provide links to their details.
    """
    genres = get_genre_lists()
    print(genres)

    # Get the selected genre ID from the query string
    selected_genre_id = request.GET.get('genre_id', None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)
    print(selected_genre_id)

    movies = []
    if selected_genre_id:
        # If a genre is selected, get the list of movies for that genre
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                movies.append({
                    'id': data.get('id'),  # Use the ID from the API response
                    'title': data.get('title'),
                    'genre': selected_genre_id,
                    'rating': data.get('vote_average'),
                    'overview': data.get('overview'),
                    'release_date': data.get('release_date')
                })

    print(movies)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'selected_genre_id': selected_genre_id
    })


def movie_details(request, movie_id):
    """
    View to display the details of a specific movie, including its overview.
    """
    movie = get_movie_details(movie_id)
    print(movie)

    if not movie:
        return render(request, 'movies/error.html', {
            'message': 'Could not fetch movie details. Please try again later.'
        })

    return render(request, 'movies/movie_details.html', {
        'title': movie.get('title'),
        'overview': movie.get('overview'),
        'release_date': movie.get('release_date'),
        'rating': movie.get('vote_average'),
        'genres': [genre['name'] for genre in movie.get('genres', [])]
    })