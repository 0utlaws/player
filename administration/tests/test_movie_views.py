import io

from PIL import Image
from django.test import TestCase, Client
from django.urls import reverse

from movies.models import Movie
from movies.tests.factories import MovieFactory, ActorFactory, CategoryFactory


class TestMovieViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_movie_url = reverse('administration:add-movie')

    def generate_image_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_movie_list_view(self):
        url = reverse('administration:movie-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/movie_list.html')

    def test_movie_create_view(self):
        response = self.client.get(self.add_movie_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_movie_create_form_valid(self):
        category = CategoryFactory()
        actor1 = ActorFactory()
        actor2 = ActorFactory()
        form_data = {
            "file": self.generate_image_file(),
            "title": "Jumanji: Welcome to the Jungle",
            "description": "The story focuses on a group of teenagers who come across Jumanji",
            "category": category.id,
            "actors": [actor1.id, actor2.id]
        }
        response = self.client.post(self.add_movie_url, form_data)
        self.assertEqual(response.status_code, 302)
        movie = Movie.objects.last()
        self.assertEqual(movie.title, "Jumanji: Welcome to the Jungle")
        self.assertEqual(movie.description, "The story focuses on a group of teenagers who come across Jumanji")

    def test_movie_update_view(self):
        movie = MovieFactory()
        url = reverse("administration:update-movie", kwargs={"pk": movie.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_movie_update_form_valid(self):
        actor1 = ActorFactory()
        actor2 = ActorFactory()
        movie = MovieFactory(actors=[actor1, actor2])
        form_data = {
            "file": self.generate_image_file(),
            "title": "New title",
            "description": "New description",
            "category": movie.category.id,
            "actors": [actor.id for actor in movie.actors.all()]
        }
        url = reverse("administration:update-movie", kwargs={"pk": movie.pk})
        self.client.post(url, form_data)
        movie.refresh_from_db()
        self.assertEqual(movie.title, "New title")
        self.assertEqual(movie.description, "New description")

    def test_movie_delete_view(self):
        movie = MovieFactory()
        url = reverse("administration:delete-movie", kwargs={"pk": movie.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form_delete.html')
