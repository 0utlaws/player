from django.test import SimpleTestCase
from django.urls import reverse, resolve

from administration.views import category_views


class TestCategoryUrls(SimpleTestCase):

    def test_category_list_url_resolves(self):
        url = reverse('administration:category-list')
        self.assertEqual(resolve(url).func.view_class, category_views.CategoryListView)

    def test_add_category_url_resolves(self):
        url = reverse('administration:add-category')
        self.assertEqual(resolve(url).func.view_class, category_views.CategoryCreateView)

    def test_update_category_url_resolves(self):
        url = reverse('administration:update-category', args=['2'])
        self.assertEqual(resolve(url).func.view_class, category_views.CategoryUpdateView)

    def test_delete_category_url_resolves(self):
        url = reverse('administration:delete-category', args=['2'])
        self.assertEqual(resolve(url).func.view_class, category_views.CategoryDeleteView)