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