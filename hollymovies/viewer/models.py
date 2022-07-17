from django.db import models
from .constants import COUNTRIES_CHOICES


class Director(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    bio = models.TextField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateField()
    bio = models.TextField()
    country_of_birth = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    description = models.TextField()
    average_rating = models.FloatField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True, blank=True)
    language = models.CharField(max_length=30, default='english')
    trailer_link = models.URLField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True)
    country_of_origin = models.CharField(max_length=30, choices=COUNTRIES_CHOICES, default='US')
    actors = models.ManyToManyField(Actor)

    # cast ???
    # production companies ???
    # image ????

    def __str__(self):
        return self.title


