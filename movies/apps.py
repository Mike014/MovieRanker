"""
This module contains the configuration for the Movies app.

Imports:
    AppConfig (django.apps.AppConfig): The base class for configuring a Django app.
"""

from django.apps import AppConfig


class MoviesConfig(AppConfig):
    """
    This class represents the configuration for the Movies app.

    Attributes:
        default_auto_field (str): The default type for auto-created primary keys.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "movies"
