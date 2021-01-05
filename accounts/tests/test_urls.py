from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts import views


class TestUrls(SimpleTestCase):
    def test_sign_up_url_resolves(self):
        url = reverse('accounts:sign-up')
        self.assertEqual(resolve(url).func.view_class, views.SignUp)

    def test_sign_in_url_resolves(self):
        url = reverse('accounts:sign-in')
        self.assertEquals(resolve(url).func.view_class, views.SignIn)

    def test_change_password_url_resolves(self):
        url = reverse('accounts:change-password')
        self.assertEquals(resolve(url).func.view_class, views.ChangePassword)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func.view_class, views.Logout)