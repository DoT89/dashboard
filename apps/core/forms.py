from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    domain = CharFilter(field_name='prj_domain', lookup_expr='icontains')

	class Meta:
		model = Project
		fields = '__all__'