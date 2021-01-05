from django.test import SimpleTestCase
from django.urls import reverse, resolve

from administration.views import access_views


class TestAccessUrls(SimpleTestCase):

    def test_access_list_url_resolves(self):
        url = reverse('administration:access-list')
        self.assertEqual(resolve(url).func.view_class, access_views.AccessListView)

    def test_add_access_url_resolves(self):
        url = reverse('administration:add-access')
        self.assertEqual(resolve(url).func.view_class, access_views.AccessCreateView)

    def test_update_access_url_resolves(self):
        url = reverse('administration:update-access', args=['2'])
        self.assertEqual(resolve(url).func.view_class, access_views.AccessUpdateView)

    def test_delete_access_url_resolves(self):
        url = reverse('administration:delete-access', args=['2'])
        self.assertEqual(resolve(url).func.view_class, access_views.AccessDeleteView)
