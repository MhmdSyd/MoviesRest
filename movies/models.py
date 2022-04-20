from django.db import models

# Create your models here.
class MoviesRest(models.Model):
    show_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    count = models.IntegerField()
    poster = models.TextField()

    class Meta:
        verbose_name = "Movie"
        ordering = ['-year',"-rating"]
        