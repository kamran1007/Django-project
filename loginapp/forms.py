from django.core import validators
from django import forms
from .models import User


class Userforms(forms.Form):
	class Meta:
		model = User
		fields = '__all__'
			