import django_filters
from .models import *

class DomainFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['prj_id']
