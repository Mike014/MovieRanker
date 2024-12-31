# Recap: This file is used to define functions that interact with The Movie Database API.
# The functions in this file are used to get the genre list, the list of movies for a specific genre, and the details of a specific movie.
# The get_genre_lists() function is used to get the genre list. It takes the API key and language as arguments.
# The get_movie_lists() function is used to get the list of movies for a specific genre. It takes the genre ID, API key, language, sorting, page, and minimum number of votes as arguments.
# The get_movie_details() function is used to get the details of a specific movie. It takes the movie ID, API key, and language as arguments.
# Changes: 31/12/2024
# In this file, we define three functions: one to get the genre list, one to get the list of movies for a specific genre, and one to get the details of a specific movie.
# The get_genre_lists() function will return a list of genres.
# The get_movie_lists() function will return a list of movies for a specific genre.
# The get_movie_details() function will return the details of a specific movie.

import os
from dotenv import load_dotenv
import requests

load_dotenv()

# API key for The Movie Database
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Function to get the genre list
def get_genre_lists():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('genres', [])
    else:
        print(f"Error fetching genres: {response.status_code}")
        return []

# Function to get the list of movies for a specific genre
def get_movie_lists(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'with_genres': genre_id,  # Pass the genre ID here
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'vote_average.desc',  # Sort by highest rating
        'page': 1,
        'vote_count.gte': 50,  # Filter by minimum number of votes
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Error fetching movies: {response.status_code}")
        return []

# Function to get the details of a specific movie
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching movie details: {response.status_code}")
        return {}

# Example usage
# if __name__ == "__main__":
#     genres = get_genre_lists()
#     if genres:
#         print("Available Genres:")
#         for genre in genres:
#             print(f"ID: {genre['id']}, Name: {genre['name']}")

#         # Choose a genre ID (manual selection or dynamic input)
#         selected_genre_id = input("Enter the genre ID: ")

#         # Get movies for the selected genre
#         movies = get_movie_lists(selected_genre_id)
#         print("\nTop Movies:")
#         for movie in movies:
#             print(f"Title: {movie['title']}, Rating: {movie['vote_average']}")
#     else:
#         print("No genres available.")