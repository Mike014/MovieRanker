"""
This module contains the views for the Movies app.

Imports:
    render (django.shortcuts.render): A function to render templates with context.
    get_genre_lists (movies.api.get_genre_lists): A utility function to fetch movie genres from an external API.
    get_movie_details (movies.api.get_movie_details): A utility function to fetch movie details from an external API.
    get_movie_lists (movies.api.get_movie_lists): A utility function to fetch movies for a specific genre from an external API.
    Movie (movies.models.Movie): The Movie model from the current app's models.

Functions:
    movie_list(request): View to display a list of movies filtered by genre.
    movie_details(request, movie_id): View to display the details of a specific movie, including its overview.
"""

from django.shortcuts import redirect, render

from .api import get_genre_lists, get_movie_details, get_movie_lists
from .models import Movie


def movie_list(request):
    """
    View to display a list of movies filtered by genre.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    genres = get_genre_lists()
    selected_genre_id = request.GET.get("genre_id", None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)

    movies = []
    if selected_genre_id:
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                movie = Movie(
                    id=data.get("id"),  # Ensure the movie ID is set
                    title=data.get("title"),
                    genre=selected_genre_id,
                    rating=data.get("vote_average"),
                    overview=data.get("overview"),
                    release_date=data.get("release_date"),
                    affiliate_link=data.get("affiliate_link"),
                )
                movies.append(movie)

    if not request.user.is_authenticated:
        movies = movies[:5]

    sponsored_movies = Movie.objects.filter(is_sponsored=True)

    return render(
        request,
        "movies/home.html",
        {
            "genres": genres,
            "movies": movies,
            "sponsored_movies": sponsored_movies,
        },
    )


def home_view(request):
    genres = get_genre_lists()
    selected_genre_id = request.GET.get("genre_id", None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)

    movies = []
    if selected_genre_id:
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                movie = Movie(
                    id=data.get("id"),  # Ensure the movie ID is set
                    title=data.get("title"),
                    genre=selected_genre_id,
                    rating=data.get("vote_average"),
                    overview=data.get("overview"),
                    release_date=data.get("release_date"),
                    affiliate_link=data.get("affiliate_link"),
                )
                movies.append(movie)

    if not request.user.is_authenticated:
        movies = movies[:5]

    sponsored_movies = Movie.objects.filter(is_sponsored=True)

    return render(
        request,
        "movies/home.html",
        {
            "movies": movies,
            "genres": genres,
            "selected_genre_id": selected_genre_id,
            "sponsored_movies": sponsored_movies,
        },
    )


def user_profile(request):
    return render(request, "movies/user_profile.html")


def subscribe(request):
    if request.method == "POST":
        return redirect("user_profile")
    return render(request, "movies/subscribe.html")


def movie_details(request, movie_id):
    """
    View to display the details of a specific movie, including its overview.

    Args:
        request (HttpRequest): The request object.
        movie_id (int): The ID of the movie to fetch details for.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    movie = get_movie_details(movie_id)
    print(movie)

    if not movie:
        return render(
            request,
            "movies/error.html",
            {"message": "Could not fetch movie details. Please try again later."},
        )

    return render(
        request,
        "movies/movie_details.html",
        {
            "title": movie.get("title"),
            "overview": movie.get("overview"),
            "release_date": movie.get("release_date"),
            "rating": movie.get("vote_average"),
            "genres": [genre["name"] for genre in movie.get("genres", [])],
        },
    )


# Recap:
# This file contains the view functions for the Movie Ranker application. It includes:

# movie_list: Displays a list of movies filtered by genre. Limits results to 5 for unauthenticated users.
# home_view: Displays the home page with sponsored movies.
# user_profile: Displays the user profile page.
# subscribe: Handles the subscription process and redirects to the user profile page upon successful subscription.
