from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from administration.forms import TicketForm, TicketMessageForm
from administration.models import Ticket, TicketMessage
from . import models, filters


class MovieCategoriesView(View):
    def get(self, request):
        return render(request, 'movies/categories.html', {
            'categories': models.Category.objects.all()
        })


class CategoryVideosView(LoginRequiredMixin, View):
    login_url = 'accounts:sign-in'

    def get(self, request, pk):
        category = models.Category.objects.get(pk=pk)
        movies = models.Movie.objects.filter(category=category)
        movies_filter = filters.MovieFilter(request.GET, queryset=movies)
        return render(request, 'movies/movies.html', {
            'filter': movies_filter
        })


class ValidateUserAccess(View):
    def get(self, request):
        movie_pk = request.GET['pk']
        data = {
            'access': models.Access.objects.filter(user=request.user, movie=movie_pk, has_access=True).exists()
        }
        return JsonResponse(data)


class VideoView(LoginRequiredMixin, View):

    def get(self, request, pk):
        return render(request, 'movies/video.html', {
            'movie': models.Movie.objects.get(pk=pk)
        })


class TicketListView(LoginRequiredMixin, View):
    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        return render(request, 'movies/ticket_list.html', {
            'tickets': tickets
        })


class TicketCreateView(View):
    def get(self, request):
        return render(request, 'movies/form.html', {
            'form': TicketForm()
        })

    def post(self, request):
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.add_message(request, messages.SUCCESS, 'Your application has been sent!')
            return redirect('movies:add-ticket')
        return redirect('movies:add-ticket')


class TicketMessageListView(View):
    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        return render(request, 'movies/ticket_message_list.html', {
            'ticket_messages': TicketMessage.objects.filter(ticket=ticket),
            'form': TicketMessageForm()
        })

    def post(self, request, pk):
        form = TicketMessageForm(data=request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.ticket = Ticket.objects.get(pk=pk)
            new_message.creator = request.user
            new_message.save()
            messages.add_message(request, messages.SUCCESS, 'Message sent!')
            return redirect('movies:ticket-messages', pk=pk)
        return redirect('movies:ticket-messages', pk=pk)