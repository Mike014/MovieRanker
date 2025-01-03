# Recap of Files and New Features in `monetization_features` Branch

## urls.py
This file defines the URL patterns for the Movie Ranker application. It includes:
- The main movie list view (`movie_list`).
- The home view (`home`).
- The user profile view (`user_profile`).
- The subscription view (`subscribe`).
- The movie details view (`movie_details`).

New Features:
- Added URL patterns for the new views related to monetization features.

## movie_list.html
This HTML file represents the main page for viewing movies filtered by genre. It includes:
- A form for selecting the genre.
- A list of filtered movies.
- A section for sponsored movies.
- An ad banner that changes based on the selected genre.
- If there are no movies for the selected genre, an appropriate message is displayed.

New Features:
- Added affiliate links for movies.
- Added a section for sponsored movies.
- Added dynamic ad banners based on the selected genre.

## user_profile.html
This HTML file represents the user profile page for the Movie Ranker application. It includes:
- A welcome message displaying the username of the logged-in user.
- A section promoting the premium subscription.
- A form that allows the user to subscribe to the premium service.

New Features:
- Added a section for premium subscription.
- Added a form to handle premium subscription.

## home.html
This HTML file represents the home page for the Movie Ranker application. It includes:
- Navigation links to other pages.
- A form for selecting the genre.
- A list of filtered movies.
- A section for sponsored movies.
- An ad banner that changes based on the selected genre.

New Features:
- Added navigation links to user profile and subscription pages.
- Added affiliate links for movies.
- Added a section for sponsored movies.
- Added dynamic ad banners based on the selected genre.

## subscribe.html
This HTML file represents the subscription page for the Movie Ranker application. It includes:
- A section promoting the premium subscription.
- A form that allows the user to subscribe to the premium service.

New Features:
- Added a form to handle premium subscription.

## views.py
This file contains the view functions for the Movie Ranker application. It includes:
- `movie_list`: Displays a list of movies filtered by genre. Limits results to 5 for unauthenticated users.
- `home_view`: Displays the home page with sponsored movies.
- `user_profile`: Displays the user profile page.
- `subscribe`: Handles the subscription process and redirects to the user profile page upon successful subscription.
- `movie_details`: Displays the details of a specific movie.

New Features:
- Added view functions to handle premium subscription and display sponsored movies.

## api.py
This file is used to define functions that interact with The Movie Database API. It includes:
- Functions to get the genre list.
- Functions to get the list of movies for a specific genre.
- Functions to get the details of a specific movie.

New Features:
- Integrated TMDB API to fetch movie details and affiliate links.

## models.py
This file is used to define the models for the movie app. It includes:
- The `Movie` model to represent a movie in the database.
- Fields for the title, genre, rating, overview, and release date of the movie.

New Features:
- Added `affiliate_link` field to the `Movie` model.
- Added `is_sponsored` field to the `Movie` model to indicate sponsored movies.

## Summary of New Features in `monetization_features` Branch
- **Affiliate Marketing**: Added affiliate links for movies.
- **Premium Subscription**: Added premium subscription functionality.
- **Advertisements**: Added dynamic ad banners based on the selected genre.
- **Sponsorships**: Added a section for sponsored movies.
