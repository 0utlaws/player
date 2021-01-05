from administration.models import Ticket


def get_open_tickets_amount(request):
    return {
        'tickets_amount': Ticket.objects.exclude(status='ended').count()
    }
