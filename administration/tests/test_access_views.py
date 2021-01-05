from django.test import TestCase, Client
from django.urls import reverse

from movies.models import Access
from movies.tests.factories import AccessFactory, MovieFactory, UserFactory, ActorFactory


class TestAccessViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_access_url = reverse('administration:add-access')

    def test_accesses_list_view(self):
        response = self.client.get(reverse("administration:access-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/access_list.html')

    def test_category_create_view(self):
        response = self.client.get(self.add_access_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_access_create_form_valid(self):
        user = UserFactory()
        actor1 = ActorFactory()
        actor2 = ActorFactory()
        movie = MovieFactory(actors=[actor1, actor2])
        form_data = {
            "movie": movie.id,
            "user": user.id,
            "has_access": True
        }
        response = self.client.post(self.add_access_url, form_data)
        self.assertEqual(response.status_code, 302)
        access = Access.objects.last()
        self.assertEqual(access.has_access, True)

    def test_access_update_view(self):
        access = AccessFactory()
        url = reverse("administration:update-access", kwargs={"pk": access.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_access_update_form_valid(self):
        access = AccessFactory(has_access=False)
        form_data = {
            "movie": access.movie.id,
            "user": access.user.id,
            "has_access": True
        }
        url = reverse("administration:update-access", kwargs={"pk": access.pk})
        self.client.post(url, form_data)
        access.refresh_from_db()
        self.assertEqual(access.has_access, True)

    def test_access_delete_view(self):
        access = AccessFactory()
        url = reverse("administration:delete-access", kwargs={"pk": access.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form_delete.html')