from django import forms
from .models import *
from .forms import *

# class ProjectForm(forms.ModelForm):
#     domain = CharFilter(field_name='prj_domain', lookup_expr='icontains')

#     class Meta:
#         model = Project
#         fields = '__all__'

class Dropdown_Domains(forms.Form):
    domains = forms.ModelChoiceField(
        queryset=Domains.objects.values_list("dom_name", flat=True).distinct(),
        empty_label=None
    )

class Dropdown_Tshirt_Sizes(forms.Form):
	sizes = forms.ModelChoiceField(
		queryset=TshirtSizes.objects.values_list("tshirt_name", flat=True).distinct(),
		empty_label=None
	)

class Dropdown_States(forms.Form):
	states = forms.ModelChoiceField(
		queryset=ProcessStates.objects.values_list("state_name", flat=True).distinct(),
		empty_label=None
	)
