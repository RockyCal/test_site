from django.db import models

from django.utils import timezone

import datetime

class File(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=20)
    isabox = models.BooleanField()
    def __unicode__(self):
        return self.name

class Employee(Owner):
    id_number = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Box(Owner):
    location = models.ForeignKey(Location)
    class Meta:
        verbose_name_plural = "Boxes"
    def __unicode__(self):
        return self.name

class Harddrive(models.Model):
    serial_number = models.CharField(max_length=20)
    startup_date = models.DateTimeField('startup date')
    owner = models.ForeignKey(Owner)
    file = models.ForeignKey(File)

    def __unicode__(self):
        return self.serial_number
    def in_box(self):
        return ( self.owner.isabox )
    def where_am_i(self):
        return self.box.location.name


class History(models.Model):
    date = models.DateTimeField()
    newowner = models.ForeignKey(Owner, related_name='history_newowner')
    oldowner = models.ForeignKey(Owner, related_name='history_oldowner')
    harddrive = models.ForeignKey(Harddrive)
    class Meta:
        ordering = ['-date']

