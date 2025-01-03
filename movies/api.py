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
# from justwatch import JustWatch

load_dotenv()

JUSTWATCH_API_URL = "https://apis.justwatch.com/content/titles/en_US/popular"

# API key for The Movie Database
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

if not TMDB_API_KEY:
    raise ValueError("TMDB_API_KEY not found in environment variables.")
else:
    print("TMDB_API_KEY loaded successfully.")

# Function to get the genre list
def get_genre_lists():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json().get('genres', [])
        if not genres:
            print("Debug: No genres received from TMDB API.")
        else:
            print(f"Debug: Received genres from TMDB API: {genres}")
        return genres
    else:
        print(f"Error fetching genres: {response.status_code}")
        return []

# Function to get the list of movies for a specific genre
def get_movie_lists(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        'with_genres': genre_id,
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'vote_average.desc',
        'page': 1,
        'vote_count.gte': 50,
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

# Function to get JustWatch links for a movie
def get_justwatch_links(movie_title):
    url = "https://apis.justwatch.com/content/titles/en_US/popular"
    params = {
        'query': movie_title
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get('items', [])
        if results:
            # Assuming the first result is the most relevant
            movie = results[0]
            streaming_info = movie.get('offers', [])
            links = [offer.get('urls', {}).get('standard_web') for offer in streaming_info if offer.get('urls')]
            return links
    return []

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

# Recap:
# This Python file contains functions to interact with The Movie Database (TMDB) API. It includes:

# Loading environment variables using dotenv to get the TMDB API key.
# Function get_genre_lists: Fetches the list of movie genres from TMDB.
# Function get_movie_lists: Fetches a list of movies for a specific genre from TMDB.
# Example usage: Demonstrates how to use the above 
# functions to print available genres and top movies for a selected genre. 
# The script prints the available genres, prompts the user to enter a genre ID, 
# and then prints the top movies for that genre.
