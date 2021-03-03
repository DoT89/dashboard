from django.db import models
import datetime

# Create your models here.
class Domains(models.Model):
    dom_id = models.IntegerField(primary_key=True, unique=True)
    dom_name = models.CharField(max_length=100)
    dom_domain_lead = models.CharField(max_length=100)
    dom_createdate = models.DateTimeField(auto_now_add=True, blank=False)
    dom_updated = models.DateTimeField(auto_now=True, blank=False)

class TshirtSizes(models.Model):
    tshirt_id = models.IntegerField(primary_key=True, unique=True)
    tshirt_name = models.CharField(max_length=3)
    tshirt_lower_limit = models.IntegerField()
    tshirt_upper_limit = models.IntegerField()
    tshirt_planning_budget = models.IntegerField()
    tshirt_createdate = models.DateTimeField(auto_now_add=True, blank=True)
    tshirt_updated = models.DateTimeField(auto_now=True, blank=False)

class ProcessStates(models.Model):
    state_id = models.IntegerField(primary_key=True, unique=True)
    state_name = models.CharField(max_length=100)
    state_order = models.IntegerField(null=False, unique=True)
    state_createdate = models.DateTimeField(auto_now_add=True, blank=False)
    state_updated = models.DateTimeField(auto_now=True, blank=False)  

class Project(models.Model):
    prj_id = models.IntegerField(primary_key=True, unique=True)
    prj_title = models.CharField(max_length=100, default='tbd')
    prj_domain = models.ForeignKey(Domains, on_delete=models.CASCADE)
    prj_size = models.ForeignKey(TshirtSizes, on_delete=models.CASCADE)
    prj_state = models.ForeignKey(ProcessStates, on_delete=models.CASCADE)
    prj_estimation = models.FloatField(null=True)
    prj_createdate = models.DateTimeField(auto_now_add=True, blank=False)
    prj_updated = models.DateTimeField(auto_now=True, blank=False)
    