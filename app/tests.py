# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from app.models import *
import datetime


class IndexViewTests(TestCase):
    def test_index_view_with_no_tickets(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Заполните форму поиска")
        self.assertEqual(response.context['index_flag'], True)


class ModelTests(TestCase):
    def test_trip_creation(self):
        trip = add_trip('TestCity', 'TestTown', datetime.time(11, 11), datetime.time(21, 21), '2000-10-20')
        trip.save()
        self.assertEqual(str(trip), 'TestCity-TestTown-2000-10-20')
        self.assertEqual(str(trip.start_time), '11:11:00')
        self.assertEqual(str(trip.duration), '10:10:00')
        self.assertEqual(str(trip.seats), '0')


def add_trip(start_point, end_point, start_time, end_time, trip_date, seats=0):
    t = Trip(
        start_point=start_point,
        end_point=end_point,
        start_time=start_time,
        end_time=end_time,
        date=trip_date,
        seats=seats
    )
    t.save()
    return t
