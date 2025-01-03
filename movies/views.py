from django.shortcuts import render, redirect
from .api import get_movie_lists, get_genre_lists
from .models import Movie

def movie_list(request):
    genres = get_genre_lists()
    selected_genre_id = request.GET.get('genre_id', None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)

    movies = []
    if selected_genre_id:
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                movie = Movie(
                    title=data.get('title'),
                    genre=selected_genre_id,
                    rating=data.get('vote_average'),
                    overview=data.get('overview'),
                    release_date=data.get('release_date'),
                    affiliate_link=data.get('affiliate_link')
                )
                movies.append(movie)

    if not request.user.is_authenticated:
        movies = movies[:5]

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'selected_genre_id': selected_genre_id
    })

def home_view(request):
    genres = get_genre_lists()
    selected_genre_id = request.GET.get('genre_id', None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)

    movies = []
    if selected_genre_id:
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                movie = Movie(
                    title=data.get('title'),
                    genre=selected_genre_id,
                    rating=data.get('vote_average'),
                    overview=data.get('overview'),
                    release_date=data.get('release_date'),
                    affiliate_link=data.get('affiliate_link')
                )
                movies.append(movie)

    if not request.user.is_authenticated:
        movies = movies[:5]

    sponsored_movies = Movie.objects.filter(is_sponsored=True)

    return render(request, 'movies/home.html', {
        'movies': movies,
        'genres': genres,
        'selected_genre_id': selected_genre_id,
        'sponsored_movies': sponsored_movies
    })

def user_profile(request):
    return render(request, 'movies/user_profile.html')

def subscribe(request):
    if request.method == 'POST':
        return redirect('user_profile')
    return render(request, 'movies/subscribe.html')
# Recap: 
# This file contains the view functions for the Movie Ranker application. It includes:

# movie_list: Displays a list of movies filtered by genre. Limits results to 5 for unauthenticated users.
# home_view: Displays the home page with sponsored movies.
# user_profile: Displays the user profile page.
# subscribe: Handles the subscription process and redirects to the user profile page upon successful subscription.