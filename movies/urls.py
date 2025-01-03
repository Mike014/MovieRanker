from django.urls import path
from . import views

urlpatterns = []

# Check if the views exist before adding them to urlpatterns
if hasattr(views, 'home_view'):
    urlpatterns.append(path('', views.home_view, name='home'))
else:
    print("Warning: 'home_view' does not exist in views.")

if hasattr(views, 'user_profile'):
    urlpatterns.append(path('profile/', views.user_profile, name='user_profile'))
else:
    print("Warning: 'user_profile' does not exist in views.")

if hasattr(views, 'subscribe'):
    urlpatterns.append(path('subscribe/', views.subscribe, name='subscribe'))
else:
    print("Warning: 'subscribe' does not exist in views.")

# Recap:
# The main movie list view (movie_list).
# The home view (home).
# The user profile view (user_profile).
# The subscription view (subscribe).
# The URL patterns are defined in the urlpatterns list.

