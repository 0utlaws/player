from django.test import TestCase, Client
from django.urls import reverse

from movies.models import Category
from movies.tests.factories import CategoryFactory


class TestCategoryViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.add_category_url = reverse('administration:add-category')

    def test_category_list_view(self):
        response = self.client.get(reverse("administration:category-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/category_list.html')

    def test_category_create_view(self):
        response = self.client.get(self.add_category_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_category_create_form_valid(self):
        response = self.client.post(self.add_category_url, data={
            "name": "adventure",
            "description": "Adventure films are a genre of film whose plots feature elements of travel."
        })
        self.assertEqual(response.status_code, 302)
        category = Category.objects.last()
        self.assertEqual(category.name, "adventure")
        self.assertEqual(category.description, "Adventure films are a genre of film whose plots feature elements of travel.")

    def test_category_update_view(self):
        category = CategoryFactory()
        url = reverse("administration:update-category", kwargs={"pk": category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form.html')

    def test_category_update_form_valid(self):
        category = CategoryFactory()
        form_data = {
            "name": category.name,
            "description": "Something new"
        }
        url = reverse("administration:update-category", kwargs={"pk": category.pk})
        self.client.post(url, form_data)
        category.refresh_from_db()
        self.assertEqual(category.description, "Something new")

    def test_category_delete_view(self):
        category = CategoryFactory()
        url = reverse("administration:delete-category", kwargs={"pk": category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administration/form_delete.html')
