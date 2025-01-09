"""
This module contains the test cases for the Movies app.

Imports:
    TestCase (django.test.TestCase): The base class for writing test cases in Django.
    reverse (django.urls.reverse): A function to reverse-resolve URL names into URL paths.
    Movie (movies.models.Movie): The Movie model from the current app's models.
    Client (django.test.Client): A class to simulate a user interacting with the code at the view level.
"""

from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from .models import Movie


class MovieModelTests(TestCase):
    """
    Test case for the Movie model.
    """

    def setUp(self):
        """
        Set up a sample movie for testing.
        """
        self.movie = Movie.objects.create(
            title="Inception",
            genre="Sci-Fi",
            rating=8.8,
            overview="A mind-bending thriller",
            release_date="2010-07-16",
            affiliate_link="http://example.com",
            is_sponsored=True,
        )

    def test_movie_str(self):
        """
        Test the string representation of the Movie instance.
        """
        self.assertEqual(str(self.movie), "Inception")

    def test_movie_fields(self):
        """
        Test the fields of the Movie instance.
        """
        self.assertEqual(self.movie.title, "Inception")
        self.assertEqual(self.movie.genre, "Sci-Fi")
        self.assertEqual(self.movie.rating, 8.8)
        self.assertEqual(self.movie.overview, "A mind-bending thriller")
        self.assertEqual(self.movie.release_date, "2010-07-16")
        self.assertEqual(self.movie.affiliate_link, "http://example.com")
        self.assertTrue(self.movie.is_sponsored)


class MovieViewsTests(TestCase):
    """
    Test case for the views in the Movies app.
    """

    def setUp(self):
        """
        Set up the test client and sample data.
        """
        self.client = Client()
        self.movie = Movie.objects.create(
            title="Inception",
            genre="Sci-Fi",
            rating=8.8,
            overview="A mind-bending thriller",
            release_date="2010-07-16",
            affiliate_link="http://example.com",
            is_sponsored=True,
        )

    def test_home_view(self):
        """
        Test the home view.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/home.html")
        self.assertContains(response, "Welcome to Movie Ranker")

    def test_movie_list_view(self):
        """
        Test the movie list view.
        """
        response = self.client.get(reverse("movie_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/home.html")
        self.assertContains(response, "Sponsored Movies")

    @patch("movies.views.get_movie_details")
    def test_movie_details_view(self, mock_get_movie_details):
        """
        Test the movie details view.
        """
        # Mock the API response
        mock_get_movie_details.return_value = {
            "title": "Inception",
            "overview": "A mind-bending thriller",
            "release_date": "2010-07-16",
            "vote_average": 8.8,
            "genres": [{"name": "Sci-Fi"}],
        }
        response = self.client.get(reverse("movie_details", args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/movie_details.html")
        self.assertContains(response, "Inception")
        self.assertContains(response, "A mind-bending thriller")
        self.assertContains(response, "2010-07-16")
        self.assertContains(response, "8.8")
        self.assertContains(response, "Sci-Fi")

    def test_user_profile_view(self):
        """
        Test the user profile view.
        """
        response = self.client.get(reverse("user_profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/user_profile.html")
        self.assertContains(response, "User Profile")

    def test_subscribe_view(self):
        """
        Test the subscribe view.
        """
        response = self.client.get(reverse("subscribe"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/subscribe.html")
        self.assertContains(response, "Subscribe to Premium")

        response = self.client.post(reverse("subscribe"))
        self.assertRedirects(response, reverse("user_profile"))
