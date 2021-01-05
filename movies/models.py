from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):
    class CategoryName(models.TextChoices):
        ADVENTURE = "adventure", "Adventure"
        ACTION = "action", "Action"
        DOCUMENTARY = "documentary", "Documentary"
        COMEDY = "comedy", "Comedy"
        DRAMA = "drama", "Drama"
        HORROR = "horror", "Horror"
        FANTASY = "fantasy", "Fantasy"
        CRIME = "crime", "Crime"

    name = models.CharField(max_length=20, choices=CategoryName.choices)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def movies_amount(self):
        return Movie.objects.filter(category=self).count()


class Actor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_place = CountryField(blank=True)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.get_full_name()

    @property
    def show_pictures(self):
        return '\n'.join(f"{picture}" + "," for picture in Picture.objects.filter(actor=self))[:-1]


class Picture(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.image}"


class Movie(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title

    @property
    def show_actors(self):
        return '\n'.join(actor.get_full_name() + ',' for actor in Actor.objects.filter(movie=self))[:-1]


class Access(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_access = models.BooleanField()
