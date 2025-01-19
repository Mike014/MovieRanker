"""
URL Configuration for the Movies app.

This module defines the URL patterns for the Movies app, mapping URLs to the appropriate class-based views.

Functions:
    path (django.urls.path): A function to define URL patterns.
    views (movies.views): The views module containing class-based views for the Movies app.

URL Patterns:
    urlpatterns (list): A list of URL patterns that Django will use to match the requested URL to the appropriate view class.
        - "" (home): Matches the root URL and calls the HomeView class.
        - "movies/" (movie_list): Matches the URL /movies/ and calls the MovieListView class.
        - "profile/" (user_profile): Matches the URL /profile/ and calls the UserProfileView class.
        - "subscribe/" (subscribe): Matches the URL /subscribe/ and calls the SubscribeView class.
        - "movies/<int:movie_id>/" (movie_details): Matches the URL /movies/<movie_id>/ and calls the MovieDetailView class, passing the movie_id as an argument.
"""

from django.urls import path

from .views import (HomeView, LoginView, LogoutView, MovieDetailView,
                    MovieListView, SubscribeView, UserProfileView)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("movies/", MovieListView.as_view(), name="movie_list"),
    path("movies/<int:movie_id>/", MovieDetailView.as_view(), name="movie_details"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]


# Old code
# # Check if the views exist before adding them to urlpatterns
# if hasattr(views, "home_view"):
#     urlpatterns.append(path("", views.home_view, name="home"))
# else:
#     print("Warning: 'home_view' does not exist in views.")

# if hasattr(views, "movie_list"):
#     urlpatterns.append(path("movies/", views.movie_list, name="movie_list"))
# else:
#     print("Warning: 'movie_list' does not exist in views.")

# if hasattr(views, "user_profile"):
#     urlpatterns.append(path("profile/", views.user_profile, name="user_profile"))
# else:
#     print("Warning: 'user_profile' does not exist in views.")

# if hasattr(views, "subscribe"):
#     urlpatterns.append(path("subscribe/", views.subscribe, name="subscribe"))
# else:
#     print("Warning: 'subscribe' does not exist in views.")

# if hasattr(views, "movie_details"):
#     urlpatterns.append(
#         path("movies/<int:movie_id>/", views.movie_details, name="movie_details")
#     )
# else:
#     print("Warning: 'movie_details' does not exist in views.")
