# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.models import Trip, Ticket
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import helpers
from random import randint


def index(request):
    start_point = request.GET.get('from')
    end_point = request.GET.get('to')
    date = request.GET.get('date')

    start_points = Trip.objects.values('start_point').distinct()  # cache?
    end_points = Trip.objects.values('end_point').distinct()

    if start_point and end_point and date:
        start_point = start_point.upper().encode('utf-8')
        end_point = end_point.upper().encode('utf-8')
        date = date.encode('utf-8')
        formatted_date = helpers.parse_date(date)
        trips = Trip.objects.all().filter(start_point=start_point, end_point=end_point, date=formatted_date)

        context_dict = {'start_point': start_point,
                        'end_point': end_point,
                        'date': date,
                        'start_points': start_points,
                        'end_points': end_points,
                        'trips': trips}
    else:
        context_dict = {'start_points': start_points,
                        'end_points': end_points,
                        'index_flag': True}

    return render(request, 'app/index.html', context_dict)


@login_required
def buy_ticket(request):
    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        trip = Trip.objects.get(id=trip_id)
        context_dict = {'trip': trip}
        return render(request, 'app/buy_ticket.html', context_dict)


@login_required
def tickets(request):
    logged_user = request.user.username
    user = User.objects.get(username=logged_user)

    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')

        trip = Trip.objects.get(id=trip_id)
        seats = trip.seats
        if seats:
            trip.seats = seats - 1
            trip.save()

        t = Ticket(trip=trip, user=user, ticket_number=(randint(1000, 9999)))
        t.save()

    all_tickets = Ticket.objects.all().filter(user=user)
    context_dict = {'tickets': all_tickets}
    return render(request, 'app/tickets.html', context_dict)
