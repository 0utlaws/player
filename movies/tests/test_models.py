from django.test import TestCase

from movies.tests.factories import CategoryFactory, ActorFactory, MovieFactory, PictureFactory


class TestModels(TestCase):

    def test_category__str__(self):
        category = CategoryFactory()
        self.assertEquals(category.__str__(), f"{category.name}")
        self.assertEquals(str(category), f"{category.name}")

    def test_category_movies_amount(self):
        category = CategoryFactory()
        MovieFactory(category=category)
        MovieFactory(category=category)
        self.assertEquals(category.movies_amount, 2)

    def test_actor__str__(self):
        actor = ActorFactory()
        self.assertEquals(actor.__str__(), f"{actor.name} {actor.surname}")
        self.assertEquals(str(actor), f"{actor.name} {actor.surname}")

    def test_actor_show_pictures(self):
        actor = ActorFactory()
        picture1 = PictureFactory(actor=actor)
        picture2 = PictureFactory(actor=actor)
        self.assertEquals(actor.show_pictures, f"{picture1},\n{picture2}")

    def test_picture__str__(self):
        picture = PictureFactory()
        self.assertEquals(picture.__str__(), f"{picture.image}")
        self.assertEquals(str(picture), f"{picture.image}")

    def test_movie__str__(self):
        movie = MovieFactory()
        self.assertEquals(movie.__str__(), f"{movie.title}")
        self.assertEquals(str(movie), f"{movie.title}")

    def test_movie_show_actors(self):
        actor1 = ActorFactory()
        actor2 = ActorFactory()
        movie = MovieFactory(actors=[actor1, actor2])
        self.assertEquals(movie.show_actors, f"{actor1},\n{actor2}")
