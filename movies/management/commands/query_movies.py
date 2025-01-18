"""
This module defines a custom Django management command that queries movies in the database and prints their titles based on different query types, and also allows inserting and deleting movie records.

The command can be executed using the project's manage.py file:

    python manage.py query_movies --type all
    python manage.py query_movies --type filter --field title --value "Inception"
    python manage.py query_movies --type exclude --field title --value "Inception"
    python manage.py query_movies --type insert --title "New Movie" --director "Director Name" --year 2023
    python manage.py query_movies --type delete --field title --value "Inception"

Classes:
    Command -- Defines the custom management command to query, insert, and delete movies.

Functions:
    add_arguments -- Adds command-line arguments to the command.
    handle -- Main method of the command that performs the query, prints the movie titles, inserts a new movie, and deletes a movie.
"""

from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = "Query movies from the database with different query types, insert a new movie, and delete a movie"

    def add_arguments(self, parser):
        parser.add_argument(
            "--type",
            type=str,
            help="Type of query: all, filter, exclude, insert, delete",
            required=True,
        )
        parser.add_argument(
            "--field", type=str, help="Field to filter, exclude, or delete by"
        )
        parser.add_argument(
            "--value", type=str, help="Value to filter, exclude, or delete by"
        )
        parser.add_argument("--title", type=str, help="Title of the movie to insert")
        parser.add_argument(
            "--director", type=str, help="Director of the movie to insert"
        )
        parser.add_argument("--year", type=int, help="Year of the movie to insert")

    def handle(self, *args, **kwargs):
        query_type = kwargs["type"]
        field = kwargs.get("field")
        value = kwargs.get("value")
        title = kwargs.get("title")
        director = kwargs.get("director")
        year = kwargs.get("year")

        if query_type == "all":
            self.stdout.write("Querying all movies from the database:")
            movies = Movie.objects.all()
        elif query_type == "filter" and field and value:
            self.stdout.write(
                f"Querying movies from the database where {field} is {value}:"
            )
            filter_kwargs = {field: value}
            movies = Movie.objects.filter(**filter_kwargs)
        elif query_type == "exclude" and field and value:
            self.stdout.write(
                f"Querying movies from the database excluding where {field} is {value}:"
            )
            exclude_kwargs = {field: value}
            movies = Movie.objects.exclude(**exclude_kwargs)
        elif query_type == "insert" and title and director and year:
            self.stdout.write(
                f"Inserting a new movie: {title}, directed by {director}, released in {year}"
            )
            new_movie = Movie(title=title, director=director, year=year)
            new_movie.save()
            self.stdout.write(f"Movie '{title}' inserted successfully.")
            return
        elif query_type == "delete" and field and value:
            self.stdout.write(
                f"Deleting movies from the database where {field} is {value}:"
            )
            delete_kwargs = {field: value}
            movies_to_delete = Movie.objects.filter(**delete_kwargs)
            count, _ = movies_to_delete.delete()
            self.stdout.write(f"Deleted {count} movie(s) where {field} is {value}.")
            return
        else:
            self.stdout.write(
                "Invalid query type or missing field/value for filter/exclude/delete, or missing details for insert."
            )
            return

        for movie in movies:
            self.stdout.write(movie.title)
            print(movie.title)
