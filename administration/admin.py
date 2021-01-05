from django.contrib import admin

from administration import models

admin.site.register(models.Ticket)
admin.site.register(models.TicketMessage)
