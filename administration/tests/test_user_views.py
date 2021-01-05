from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from movies.tests.factories import UserFactory


class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_user_url = reverse('administration:add-user')

    def test_user_list_view(self):
        response = self.client.get(reverse("administration:user-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/user_list.html')

    def test_user_create_view(self):
        response = self.client.get(self.add_user_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_user_create_form_valid(self):
        response = self.client.post(self.add_user_url, data={
            "username": "example_username",
            "email": "email@example.com",
            "password1": "example_password",
            "password2": "example_password",
            "is_staff": True,
            "is_superuser": False
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.last()
        self.assertEqual(user.username, "example_username")

    def test_user_update_view(self):
        user = UserFactory()
        url = reverse("administration:update-user", kwargs={"pk": user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_user_update_form_valid(self):
        user = UserFactory(is_staff=True)
        form_data = {
            "username": "newusername",
            "email": "newemail@example.com",
            "password": user.password,
        }
        url = reverse("administration:update-user", kwargs={"pk": user.pk})
        self.client.post(url, form_data)
        user.refresh_from_db()
        self.assertEqual(user.username, "newusername"),
        self.assertEqual(user.email, "newemail@example.com")

    def test_user_delete_view(self):
        user = UserFactory()
        url = reverse("administration:delete-user", kwargs={"pk": user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form_delete.html')

    def test_user_change_password_view(self):
        user = UserFactory()
        url = reverse("administration:change-password", kwargs={"pk": user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('administration/change_password.html')



