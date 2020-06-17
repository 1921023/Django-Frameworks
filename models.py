from django.db import models
from django.utils import timezone



# Create your models here.

def __str__(self):
    return self.name


class Staff(models.Model):
    photo = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    experience = models.CharField(max_length=500)
    qualification = models.CharField(max_length=250)
    no_of_publications_journal = models.CharField(max_length=250)
    no_of_publications_conference = models.CharField( max_length=250)
    professional_memberships = models.CharField(max_length=250)
    research_interest = models.CharField(max_length=250)
    faculty_id=models.CharField( max_length=250)


class Network(models.Model):
    summery = models.CharField(max_length=250)
    switches = models.TextField()
    controller = models.CharField(max_length=250)
    accesspoint = models.CharField(max_length=250)
    network_id = models.CharField(default = '-', max_length=250)
