# -*- coding: utf-8 -*-
import os
import django
from random import randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board.settings')
django.setup()

from app.models import *

cities = [
    'Москва',
    'Питер',
    'Омск',
    'Самара',
    'Курск',
    'Зеленоград',
    'Ростов',
    'Белгород',
    'Волгоград',
]

DAYS = 31
TRIPS = 15


def populate():
    for day in range(1, DAYS):
        for i in range(1, TRIPS):
            start_hour = randint(6, 11)
            stop_hour = randint(12, 18)
            start_min = randint(1, 60)
            stop_min = randint(1, 60)
            start_time = str(start_hour) + ':' + str(start_min) + ':00'
            start_time = datetime.strptime(start_time, '%X').time()
            end_time = str(stop_hour) + ':' + str(stop_min) + ':00'
            end_time = datetime.strptime(end_time, '%X').time()
            trip_date = '2015-10-' + str(day)
            for start_city in cities:
                start_city = start_city.decode('utf-8')
                for stop_city in cities:
                    seats = randint(0, 10)
                    stop_city = stop_city.decode('utf-8')
                    add_trip(start_city, stop_city, start_time, end_time, trip_date, seats)


def add_trip(start_point, end_point, start_time, end_time, trip_date, seats):
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

if __name__ == '__main__':
    print "Starting population script..."
    populate()
