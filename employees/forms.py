from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('full_name', 'mobile', 'emp_code', 'position',)
        labels = {
            'full_name': 'Full Name',
            'emp_code': 'EMP. Code'
        }
        
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select Position'
        self.fields['emp_code'].required = False
        