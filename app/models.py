from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Trip(models.Model):
    start_point = models.CharField(max_length=32)
    end_point = models.CharField(max_length=32)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.TimeField()
    date = models.DateField()
    seats = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
            self.start_point = self.start_point.upper()
            self.end_point = self.end_point.upper()
            end_date = datetime.combine(date.today(), self.end_time)
            start_date = datetime.combine(date.today(), self.start_time)
            self.duration = str(end_date - start_date)
            super(Trip, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.start_point + '-' + self.end_point + '-' + str(self.date)


class Ticket(models.Model):
    trip = models.ForeignKey(Trip)
    user = models.ForeignKey(User)
    ticket_number = models.CharField(max_length=16)

    def __unicode__(self):
        return self.user.username + '-' + self.ticket_number
