from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        PENDING = 'pending', 'Pending'
        ENDED = 'ended', 'Ended'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

