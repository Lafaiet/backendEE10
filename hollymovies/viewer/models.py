from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    description = models.TextField()
    average_rating = models.FloatField()
    duration = models.PositiveIntegerField()
    # director ????
    # image ????


