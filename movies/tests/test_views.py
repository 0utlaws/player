from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from movies.tests.factories import CategoryFactory, MovieFactory, UserFactory


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('example_username', 'example_email@example.com', 'example_password')
        self.categories_url = reverse('movies:categories')
        self.category_videos_url = reverse('movies:category-videos', args=['1'])
        self.video_url = reverse('movies:video', args=['1'])
        self.validate_access_url = reverse('movies:validate-access')

    def test_categories_view(self):
        response = self.client.get(self.categories_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/categories.html')

    def test_category_videos_view(self):
        self.category = CategoryFactory()
        response = self.client.get(self.category_videos_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/movies.html')

    def test_video_view(self):
        self.client.login(username='example_username', password='example_password')
        self.movie = MovieFactory()
        response = self.client.get(self.video_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/video.html')
