from django import forms
from .models import Exam, Employee
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from django.views.generic.edit import UpdateView

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'),('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('name', 'description', 'published')



class EmployeeForm(forms.ModelForm):
    # StartDate = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
       model = Employee
       fields = (
           'EmpNo',
           'FName',
           'LName',
           'Sex',
           'Salary',
           'StartDate',
           'DeptCode'
            )
            
class EditForm(UpdateView):
    class Meta:
        model = Employee
        fields = (
           'EmpNo',
           'FName',
           'LName',
           'Sex',
           'Salary',
           'StartDate',
           'DeptCode'
            )
        template_name_suffix = '_update_form'
