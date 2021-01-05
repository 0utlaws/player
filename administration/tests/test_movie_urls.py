from django.test import SimpleTestCase
from django.urls import reverse, resolve

from administration.views import movie_views


class TestMovieUrls(SimpleTestCase):

    def test_movie_list_url_resolves(self):
        url = reverse('administration:movie-list')
        self.assertEqual(resolve(url).func.view_class, movie_views.MovieListView)

    def test_add_movie_url_resolves(self):
        url = reverse('administration:add-movie')
        self.assertEqual(resolve(url).func.view_class, movie_views.MovieCreateView)

    def test_update_movie_url_resolves(self):
        url = reverse('administration:update-movie', args=['2'])
        self.assertEqual(resolve(url).func.view_class, movie_views.MovieUpdateView)

    def test_delete_movie_url_resolves(self):
        url = reverse('administration:delete-movie', args=['2'])
        self.assertEqual(resolve(url).func.view_class, movie_views.MovieDeleteView)