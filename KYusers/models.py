from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

year_choices = [
        (None, 'year'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]
sex_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

class College(models.Model):
    collegeId = models.AutoField(primary_key=True)
    collegeName = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s- %s" %(self.collegeName, self.collegeId)


class KYProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.PositiveSmallIntegerField(null=True)
    sex = models.CharField(max_length=10, choices=sex_choices)
    year = models.PositiveSmallIntegerField(choices=year_choices)
    mobile_number = models.BigIntegerField()
    college = models.OneToOneField(College)
    # referalCode = models.Field() #should be caId of some CA.
    kyId = models.CharField(max_length=20,blank=True)

    def save(self, *args, **kwargs):
        super(KYProfile, self).save(*args, **kwargs)
        self.kyId = 'KY-%d-%04d' %(self.college.collegeId, self.id)
        super(KYProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" %self.kyId

#every CA will have KYProfile. so no need to have college (name,add again)
class CAProfile(models.Model):
    kyprofile = models.OneToOneField(KYProfile)
    collegeAddress = models.TextField()
    postalAddress = models.TextField()
    pincode = models.PositiveIntegerField()
    regNum = models.PositiveIntegerField(null=True, blank=True) #no. of refered kyprofile.

    caId = models.CharField(max_length=20,blank=True)

    def save(self, *args, **kwargs):
        super(CAProfile, self).save(*args, **kwargs)
        self.caId = 'CA-%d-%04d' % (self.kyprofile.college.collegeId, self.id)
        super(CAProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" %self.caId
