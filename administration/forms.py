from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from administration.models import Ticket, TicketMessage
from movies import models


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'is_superuser']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'is_staff', 'is_superuser', 'is_active']


class ActorForm(forms.ModelForm):
    pictures = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = models.Actor
        fields = ['name', 'surname', 'birth_place', 'pictures']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'content']


class TicketMessageForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write your message here...', 'rows': 8}))

    class Meta:
        model = TicketMessage
        fields = ['content']


class SingleEmailForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.exclude(is_staff=True))
    subject = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea())


class MultipleEmailForm(forms.Form):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.exclude(is_staff=True))
    subject = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea())
