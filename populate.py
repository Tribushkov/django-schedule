# -*- coding: utf-8 -*-
import os
from random import randint
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board.settings')

from datetime import datetime
import django
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


def populate():
    for day in range(1,31):
        for i in range (1,15):
            start_hour = randint(6, 11)
            stop_hour = randint(12, 18)
            start_min = randint(1, 59)
            stop_min = randint(1, 59)
            start_time = str(start_hour) + ':' + str(start_min) + ':00'
            start_time = datetime.strptime(start_time, '%X').time()
            end_time = str(stop_hour) + ':' + str(stop_min) + ':00'
            end_time = datetime.strptime(end_time, '%X').time()
            date = '2015-10-' + str(day)
            for start_city in cities:
                start_city = start_city.decode('utf-8').upper()
                for stop_city in cities:
                    seats = randint(0, 10)
                    stop_city = stop_city.decode('utf-8').upper()
                    add_trip(start_city, stop_city, start_time, end_time, date, seats)


def add_trip(start_point, end_point, start_time, end_time, date, seats):
    t = Trip(
        start_point = start_point,
        end_point = end_point,
        start_time = start_time,
        end_time = end_time,
        date = date,
        seats = seats
    )
    t.save()
    return t

if __name__ == '__main__':
    print "Starting population script..."
    populate()