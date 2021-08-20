from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name
    
class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    song = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)

    def __str__(self):
        return self.song