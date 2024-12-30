from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    overview = models.TextField(default='') 
    release_date = models.DateField(null=True, blank=True)
# title, genre, rating, overview, release_date are the fields of the Movie model.
    def __str__(self):
        return self.title