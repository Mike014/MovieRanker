from django.urls import path
from . import views

urlpatterns = []

# Check if the views exist before adding them to urlpatterns
if hasattr(views, 'home_view'):
    urlpatterns.append(path('', views.home_view, name='home'))
else:
    print("Warning: 'home_view' does not exist in views.")

if hasattr(views, 'movie_list'):
    urlpatterns.append(path('movies/', views.movie_list, name='movie_list'))
else:
    print("Warning: 'movie_list' does not exist in views.")

if hasattr(views, 'user_profile'):
    urlpatterns.append(path('profile/', views.user_profile, name='user_profile'))
else:
    print("Warning: 'user_profile' does not exist in views.")

if hasattr(views, 'subscribe'):
    urlpatterns.append(path('subscribe/', views.subscribe, name='subscribe'))
else:
    print("Warning: 'subscribe' does not exist in views.")

if hasattr(views, 'movie_details'):
    urlpatterns.append(path('movies/<int:movie_id>/', views.movie_details, name='movie_details'))
else:
    print("Warning: 'movie_details' does not exist in views.")

# Recap:
# The main movie list view (movie_list).
# The home view (home).
# The user profile view (user_profile).
# The subscription view (subscribe).
# The movie details view (movie_details).