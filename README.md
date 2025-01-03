# Recap of Files and New Features in `linking_movies_to` Branch

## urls.py
This file defines the URL patterns for the Movie Ranker application. It includes:
- The main movie list view (`movie_list`).
- The movie details view (`movie_details`).

New Features:
- Added URL patterns for the overwiew of the films.

## movie_list.html
This HTML file represents the main page for viewing movies filtered by genre. It includes:
- A form for selecting the genre.
- A list of filtered movies.
- A section for sponsored movies.
- An ad banner that changes based on the selected genre.
- If there are no movies for the selected genre, an appropriate message is displayed.

## movie_details.html
This HTML file who overwiew the movie choosen.

## views.py
This file contains the view functions for the Movie Ranker application. It includes:
- `movie_list`: Displays a list of movies filtered by genre. Limits results to 5 for unauthenticated users.
- `movie_details`: Displays the details of a specific movie.

## api.py
This file is used to define functions that interact with The Movie Database API. It includes:
- Functions to get the genre list.
- Functions to get the list of movies for a specific genre.
- Functions to get the details of a specific movie.

## models.py
This file is used to define the models for the movie app. It includes:
- The `Movie` model to represent a movie in the database.
- Fields for the title, genre, rating, overview, and release date of the movie.


