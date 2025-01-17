from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Query all movies from the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Querying the database:")

        # Query all movies from the database using the all() method, similar to a SELECT * query in SQL.
        movies = Movie.objects.all()

        for movie in movies:
            self.stdout.write(movie.title)
            print(movie.title)