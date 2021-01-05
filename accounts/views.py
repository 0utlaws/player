from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View


class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/sign_up.html', {
            'form': form
        })

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been created. You can sign in.')
            return redirect('accounts:sign-in')
        return render(request, 'accounts/sign_up.html', {
            'form': form
        })


class SignInView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'accounts/sing_in.html', {
            'form': form
        })

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request=request,
                username=username,
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('movies:categories')
        return render(request, 'accounts/sing_in.html', {
            'form': form
        })


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.add_message(request, messages.SUCCESS,
                                 'Your password was updated successfully! Please sign in again.')
            return redirect('accounts:sign-in')
        return render(request, 'accounts/change_password.html', {
            'form': form
        })


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:sign-in')


class PasswordResetView(View):
    success_url = reverse_lazy('account:password_reset_confirm')

    def get(self, request):
        form = PasswordResetForm()
        return render(request, 'accounts/password_reset.html', {
            'form': form
        })

    def post(self, request):
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email'])
            if user.exists():
                subject = "Password Reset"
                email_template_name = "accounts/password_reset_email.txt"
                content = {
                    "email": user[0].email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user[0].pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user[0]),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, content)
                try:
                    send_mail(subject, email, 'admin@example.com', [user[0].email], fail_silently=False)
                    return redirect('password_reset_done')
                except BadHeaderError:
                    messages.add_message(request, messages.WARNING, 'Invalid header found!')
                    return redirect('accounts:password_reset')

            messages.add_message(request, messages.WARNING, 'User with this email does not exists!')
            return redirect('accounts:password-reset')
