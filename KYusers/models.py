from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

year_choices = [
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]

class KYProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    year = models.IntegerField(choices=year_choices)
    mobile_number = models.BigIntegerField()
    college = models.CharField(max_length=250)

    def __unicode__(self):
        return  "%s" %self.user
