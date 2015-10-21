from django.contrib import admin
from app.models import Trip, Ticket


class TripAdmin(admin.ModelAdmin):
    exclude = ('slug', 'duration')
    list_display = ('date', 'start_time', 'start_point', 'end_point', 'seats')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('trip', 'user')

admin.site.register(Trip, TripAdmin)
admin.site.register(Ticket, TicketAdmin)
