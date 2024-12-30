from django.shortcuts import render
from .api import get_movie_lists, get_genre_lists
from .models import Movie

def movie_list(request):
    genres = get_genre_lists()
    
    # Get the selected genre ID from the query string
    selected_genre_id = request.GET.get('genre_id', None)
    if selected_genre_id is not None:
        selected_genre_id = int(selected_genre_id)

    movies = []
    if selected_genre_id:
        # If a genre is selected, get the list of movies for that genre
        movies_data = get_movie_lists(selected_genre_id)
        if movies_data:
            for data in movies_data:
                print(f"Title: {data.get('title')}")
                print(f"Rating: {data.get('vote_average')}")
                print(f"Release Date: {data.get('release_date')}")
                print(f"Overview: {data.get('overview')}") 

                movie = Movie(
                    title=data.get('title'),
                    genre=selected_genre_id,
                    rating=data.get('vote_average'),
                    overview=data.get('overview'),
                    release_date=data.get('release_date')
                )
                movies.append(movie)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres,
        'selected_genre_id': selected_genre_id
    })