"""
Views for the Movies app.

This module defines the class-based views (CBV) for the Movies app, handling the display of movie lists, movie details, user profiles, and subscriptions.

Imports:
    render (django.shortcuts.render): A function to render templates with context.
    redirect (django.shortcuts.redirect): A function to redirect to a different URL.
    get_genre_lists (movies.api.get_genre_lists): A utility function to fetch movie genres from an external API.
    get_movie_details (movies.api.get_movie_details): A utility function to fetch movie details from an external API.
    get_movie_lists (movies.api.get_movie_lists): A utility function to fetch movies for a specific genre from an external API.
    Movie (movies.models.Movie): The Movie model from the current app's models.
    View (django.views.View): The base class for all class-based views in Django.

Classes:
    MovieListView(View): View to display a list of movies filtered by genre.
    MovieDetailView(View): View to display the details of a specific movie, including its overview.
    UserProfileView(View): View to display the user profile page.
    SubscribeView(View): View to handle user subscriptions.
    HomeView(View): View to display the home page.
"""

from django.shortcuts import redirect, render
from django.views import View

from .api import get_genre_lists, get_movie_details, get_movie_lists
from .models import Movie


class MovieListView(View):
    def get(self, request):
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
                        id=data.get("id"),
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

        return render(
            request, "movies/movie_list.html", {"movies": movies, "genres": genres}
        )


class MovieDetailView(View):
    def get(self, request, movie_id):
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


class UserProfileView(View):
    def get(self, request):
        """
        View to display the user's profile.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response object with the rendered template.
        """
        return render(request, "movies/user_profile.html")


class SubscribeView(View):
    def post(self, request):
        """
        View to handle user subscriptions.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response object with the rendered template.
        """
        return redirect("user_profile")

    def get(self, request):
        """
        View to display the subscription form.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: The response object with the rendered template.
        """
        return render(request, "movies/subscribe.html")


class HomeView(View):
    def get(self, request):
        """
        View to display the home page with a list of movies.

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
                        id=data.get("id"),
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
