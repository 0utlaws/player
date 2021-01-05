from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = {
            'username': 'example_username',
            'password1': 'example_password',
            'password2': 'example_password'
        }
        self.sign_up_url = reverse('accounts:sign-up')
        self.sign_in_url = reverse('accounts:sign-in')

    def test_sign_up_view(self):
        response = self.client.get(self.sign_up_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_up.html')
        self.failUnless(isinstance(response.context['form'], UserCreationForm))

    def test_sign_up_form_valid(self):
        response = self.client.post(self.sign_up_url, data=self.user)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.sign_in_url)
        self.assertEqual(User.objects.count(), 1)

    def test_sign_in_view(self):
        response = self.client.get(self.sign_in_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sing_in.html')
        self.failUnless(isinstance(response.context['form'], AuthenticationForm))

    def test_sign_in_form_valid(self):
        self.client.post(self.sign_up_url, data=self.user)
        response = self.client.post(self.sign_in_url, data={
            'username': self.user['username'],
            'password': self.user['password1']
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('movies:categories'))
