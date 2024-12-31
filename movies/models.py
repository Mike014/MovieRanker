from django.db import models

# Recap: This file is used to define the models for the movie app.
# The Movie model is used to represent a movie in the database.
# The Movie model has fields for the title, genre, rating, overview, and release date of the movie.
# Changes: 31/12/2024
# In this file, we define the Movie model with five fields: title, genre, rating, overview, and release date.
# The title field is a CharField with a maximum length of 255 characters.
# The genre field is a CharField with a maximum length of 100 characters.
# The rating field is a FloatField.
# The overview field is a TextField with a default value of an empty string.
# The release_date field is a DateField that can be null or blank.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    overview = models.TextField(default='') 
    release_date = models.DateField(null=True, blank=True)
    
    # title, genre, rating, overview, release_date are the fields of the Movie model.
    def __str__(self):
        return self.title