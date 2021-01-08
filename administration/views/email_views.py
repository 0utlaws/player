from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.views import View

from administration.forms import SingleEmailForm, MultipleEmailForm


class SingleSendEmailView(View):
    def get(self, request):
        form = SingleEmailForm()
        return render(request, 'administration/form.html', {
            'form': form
        })

    def post(self, request):
        form = SingleEmailForm(data=request.POST)
        if form.is_valid():
            receiver = form.cleaned_data['user']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'admin@example.com', [receiver.email], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, 'Message has been sent!')
                return redirect('administration:single-email')
            except BadHeaderError:
                messages.add_message(request, messages.WARNING, 'Invalid header found!')
                return redirect('administration:single-email')
        messages.add_message(request, messages.WARNING, 'Invalid form!')
        return redirect('administration:single-email')


class MultipleSendEmailView(View):
    def get(self, request):
        form = MultipleEmailForm()
        return render(request, 'administration/form.html', {
            'form': form
        })

    def post(self, request):
        form = MultipleEmailForm(data=request.POST)
        if form.is_valid():
            receivers = form.cleaned_data['user']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'admin@example.com', [receiver.email for receiver in receivers], fail_silently=False)
                messages.add_message(request, messages.SUCCESS, 'Message has been sent!')
                return redirect('administration:multiple-email')
            except BadHeaderError:
                messages.add_message(request, messages.WARNING, 'Invalid header found!')
                return redirect('administration:multiple-email')
        messages.add_message(request, messages.WARNING, 'Invalid form!')
        return redirect('administration:multiple-email')