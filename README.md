# Movie Ranker Prototype

**Movie Ranker** is a prototype web application written in Django. This app is an early-stage project and is not yet deployed. Its primary goal is to serve as a dynamic movie recommendation app, designed to help users find movies to watch, tailored to their preferences.

## Overview

Currently, the app connects to The Movie Database (TMDB) API to fetch movie data and display it in a user-friendly interface. While it includes only basic features, its potential lies in evolving into a sophisticated tool for discovering movies based on genres, ranks, and similarities.

### Features

- **Integration with TMDB API**: The app fetches movie genres, ranks, and other details using TMDB API endpoints.
- **Genre Filtering**: Users can filter movies by selecting genres from a dropdown menu.
- **Dynamic Movie List**: Displays a ranked list of movies based on the selected genre.

---

## Key Components

### 1. **`api.py`**
- Acts as the bridge between the application and TMDB API.
- Contains functions to fetch genres, movies by genre, and other movie details.
- Example endpoint usage:  
  - Fetch genres: `https://api.themoviedb.org/3/genre/movie/list`
  - Fetch movies by genre: `https://api.themoviedb.org/3/discover/movie`

### 2. **`views.py`**
- Implements the app's logic for handling user requests.
- Currently includes a simple `if` condition and `for` loop to process and display movie data.
- Pulls data from `api.py` and passes it to the frontend.

### 3. **`models.py`**
- Defines the structure for storing movie data temporarily (e.g., `title`, `genre`, `rating`, etc.).

### 4. **`movie_list.html`**
- Frontend template that dynamically renders movie data using Django template language.
- Includes:
  - A form for selecting a movie genre.
  - A list that displays movies with their rank, title, and genre.

---

## Future Goals

- Enhance the logic in `views.py` to include advanced algorithms for movie similarity:
  1. **Content-Based Filtering**: Compare movies based on their `overview` and `genre`.
  2. **Collaborative Filtering**: Leverage user ratings for recommendations.
  3. **Rank and Popularity Sorting**: Prioritize movies by user ratings and number of votes.
- Dynamically generate similar movies based on:
  - Genre
  - Rank
  - Plot overview

---

## Useful TMDB API Endpoints

1. **Fetch Genre List**:  
   `https://api.themoviedb.org/3/genre/movie/list`

2. **Discover Movies by Genre**:  
   `https://api.themoviedb.org/3/discover/movie`

3. **Find Movie Details by ID**:  
   `https://api.themoviedb.org/3/movie/{movie_id}`

4. **Fetch Similar Movies**:  
   `https://api.themoviedb.org/3/movie/{movie_id}/similar`

---

## Disclaimer

This is a prototype app for demonstration and learning purposes. Further improvements, including deployment and additional features, will be implemented in future iterations.
