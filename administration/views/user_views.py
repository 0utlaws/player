from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from administration import forms


class UserListView(ListView):
    model = User
    template_name = 'administration/user_list.html'
    paginate_by = 1


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:user-list')
    success_message = "User successfully created!"
    form_class = forms.UserCreateForm


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:user-list')
    success_message = "User successfully updated!"
    form_class = forms.UserUpdateForm

    action = 'Update'


class UserChangePasswordView(View):
    def get(self, request, pk):
        form = PasswordChangeForm(user=User.objects.get(pk=pk))
        return render(request, 'administration/change_password.html', {
            'form': form,
        })

    def post(self, request, pk):
        form = PasswordChangeForm(User.objects.get(pk=pk), request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=User.objects.get(pk=pk))
            messages.add_message(request, messages.SUCCESS, 'User password was changed successfully!')
            return redirect('administration:user-list')
        messages.add_message(request, messages.WARNING, 'Failed to changed password!')
        return redirect('administration:user-list')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'administration/form_delete.html'
    success_url = reverse_lazy('administration:user-list')
    success_message = "User successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)