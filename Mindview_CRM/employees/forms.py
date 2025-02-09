from django import forms

from . import models

class EmployeesDetailsForm(forms.ModelForm):
    class Meta:
        model = models.EmployeesDetails
        exclude = ['slug']