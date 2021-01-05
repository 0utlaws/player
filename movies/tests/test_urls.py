from django.test import SimpleTestCase
from django.urls import reverse, resolve

from movies import views


class TestUrls(SimpleTestCase):

    def test_categories_url_resolves(self):
        url = reverse('movies:categories')
        self.assertEqual(resolve(url).func.view_class, views.MovieCategories)

    def test_category_videos_url_resolves(self):
        url = reverse('movies:category-videos', args=['2'])
        self.assertEqual(resolve(url).func.view_class, views.CategoryVideos)

    def test_validate_access_url_resolves(self):
        url = reverse('movies:validate-access')
        self.assertEqual(resolve(url).func.view_class, views.ValidateUserAccess)

    def test_video_url_resolves(self):
        url = reverse('movies:video', args=['3'])
        self.assertEqual(resolve(url).func.view_class, views.Video)
