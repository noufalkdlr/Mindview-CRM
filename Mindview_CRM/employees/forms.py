from django import forms

from . import models

class EmployeesDetailsForm(forms.ModelForm):
    class Meta:
        model = models.EmployeesDetails
        exclude = ['slug']
        widgets = {
            'd_o_b' : forms.DateInput(attrs={'type': 'date'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})
        }