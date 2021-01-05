from django.test import SimpleTestCase
from django.urls import reverse, resolve

from administration.views import actor_views


class TestActorUrls(SimpleTestCase):

    def test_actor_list_url_resolves(self):
        url = reverse('administration:actor-list')
        self.assertEqual(resolve(url).func.view_class, actor_views.ActorListView)

    def test_add_actor_url_resolves(self):
        url = reverse('administration:add-actor')
        self.assertEqual(resolve(url).func.view_class, actor_views.ActorCreateView)

    def test_update_actor_url_resolves(self):
        url = reverse('administration:update-actor', args=['2'])
        self.assertEqual(resolve(url).func.view_class, actor_views.ActorUpdateView)

    def test_delete_actor_url_resolves(self):
        url = reverse('administration:delete-actor', args=['2'])
        self.assertEqual(resolve(url).func.view_class, actor_views.ActorDeleteView)
