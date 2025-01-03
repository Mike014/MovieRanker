from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    overview = models.TextField(default='') 
    release_date = models.DateField(null=True, blank=True)
    # Add new fields for the affiliate link and sponsored status
    # The affiliate_link field is a URLField that stores the affiliate link for the movie.
    affiliate_link = models.URLField(blank=True, null=True)  
    is_sponsored = models.BooleanField(default=False)  
# title, genre, rating, overview, release_date are the fields of the Movie model.
    def __str__(self):
        return self.title