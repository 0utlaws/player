from django.test import TestCase, Client
from django.urls import reverse

from movies.models import Actor
from movies.tests.factories import ActorFactory


class TestActorViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_actor_url = reverse('administration:add-actor')

    def test_actor_list_view(self):
        url = reverse('administration:actor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/actor_list.html')

    def test_actor_create_view(self):
        response = self.client.get(self.add_actor_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_actor_create_form_valid(self):
        form_data = {
            "name": "Name",
            "surname": "Surname",
            "birth_place": "US"
        }
        response = self.client.post(self.add_actor_url, form_data)
        self.assertEqual(response.status_code, 302)
        actor = Actor.objects.get(name="Name")
        self.assertEqual(actor.surname, "Surname")
        self.assertEqual(actor.birth_place, "US")

    def test_actor_update_view(self):
        actor = ActorFactory()
        url = reverse("administration:update-actor", kwargs={"pk": actor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_actor_update_form_valid(self):
        actor = ActorFactory()
        self.client.post(reverse("administration:update-actor", kwargs={"pk": actor.pk}), data={
            "name": actor.name,
            "surname": "Something new",
            "birth_place": actor.birth_place
        })
        actor.refresh_from_db()
        self.assertEqual(actor.surname, "Something new")

    def test_actor_delete_view(self):
        actor = ActorFactory()
        response = self.client.get(reverse("administration:delete-actor", kwargs={"pk": actor.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form_delete.html')