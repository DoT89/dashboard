#from django.forms import ModelForm
from django import forms
from .models import *

class ProjectSubmitForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['prj_title', 'prj_domain', 'prj_size', 'prj_state']
	
class EditProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['prj_estimation']
