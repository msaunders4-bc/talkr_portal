from django import forms
from .models import Employee, Client


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name', 'email', 'client', 'acc_number', 
            'embg', 'mk_id', 'start_date', 'net_salary'
        ]
        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                },
                format='%Y-%m-%d'
            ),
            'net_salary': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'class': 'form-control'
                }
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields required except client
        for field_name, field in self.fields.items():
            if field_name != 'client':
                field.required = True
            # Add CSS classes to all fields
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'