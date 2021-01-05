from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView

from administration.forms import TicketMessageForm
from administration.models import Ticket, TicketMessage


class TicketListView(ListView):
    model = Ticket
    template_name = 'administration/ticket_list.html'
    paginate_by = 1


class TicketUpdateView(SuccessMessageMixin, UpdateView):
    model = Ticket
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:ticket-list')
    success_message = "Report successfully updated!"

    fields = [
        'status'
    ]


class TicketMessageListAndCreateView(View):
    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        return render(request, 'administration/ticket_message_list.html', {
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
            return redirect('administration:ticket-messages', pk=pk)
        return redirect('administration:ticket-messages', pk=pk)
