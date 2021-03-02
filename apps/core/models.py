from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    ESTIMATAED_TSHIRT_SIZE = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
    )

    CTO_DOMAINS = (
        ('CF', 'Corporate Functions'),
        ('CRM', 'CRM & Billing'),
        ('CE', 'Customer Engagement'),
        ('DSS', 'Data Services & Solutions'),
        ('IS', 'Infrastructure Services'),
        ('PPRM', 'Program & Product Release Management'),
    )

    STATE = (
        ('1', 'In Idea Phase'),
        ('2', 'In High Level Scoping'),
        ('3', 'In Planning'),
        ('4', 'In Delivery'),
        ('5', 'Completed'), 
    )

    prj_id = models.IntegerField(primary_key=True, unique=True)
    prj_title = models.CharField(max_length=100, default='tbd')
    prj_domain = models.CharField(max_length=4, choices=CTO_DOMAINS, default='tbd')
    prj_size = models.CharField(max_length=3, choices=ESTIMATAED_TSHIRT_SIZE, default='tbd')
    prj_state = models.CharField(max_length=1, choices=STATE, default='tbd')
    prj_estimation = models.FloatField(null=True)
    #prj_planned_delivery = models.DateField(null=True)
    #prj_createdate = models.DateTimeField(auto_now_add=True)

class Domains(models.Model):
    dom_id = models.IntegerField(primary_key=True, unique=True)
    dom_name = models.CharField(max_length=100)
    dom_domain_lead = models.CharField(max_length=100)
    dom_createdate = models.DateTimeField(auto_now_add=True, blank=True)
    dom_updated = models.DateTimeField(auto_now=True, blank=True)

