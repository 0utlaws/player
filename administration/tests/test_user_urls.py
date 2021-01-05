from django.test import SimpleTestCase
from django.urls import reverse, resolve

from administration.views import user_views


class TestUserUrls(SimpleTestCase):
    def test_user_list_url_resolves(self):
        url = reverse('administration:user-list')
        self.assertEqual(resolve(url).func.view_class, user_views.UserListView)

    def test_add_user_url_resolves(self):
        url = reverse('administration:add-user')
        self.assertEqual(resolve(url).func.view_class, user_views.UserCreateView)

    def test_update_user_url_resolves(self):
        url = reverse('administration:update-user', args=['2'])
        self.assertEqual(resolve(url).func.view_class, user_views.UserUpdateView)

    def test_delete_user_url_resolves(self):
        url = reverse('administration:delete-user', args=['2'])
        self.assertEqual(resolve(url).func.view_class, user_views.UserDeleteView)

    def test_user_change_password_url_resolves(self):
        url = reverse('administration:change-password', args=['2'])
        self.assertEqual(resolve(url).func.view_class, user_views.UserChangePasswordView)
