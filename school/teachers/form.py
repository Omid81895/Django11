from django import forms
from django.core.exceptions import ValidationError
class TeacherForm(forms.Form):
    name = forms.CharField(label='your name', label_suffix='=', max_length=25, widget=forms.TextInput({'class':'form-control'}))
    email = forms.EmailField(help_text='your email should gmail account', required=True, error_messages={'required': 'please enter your email'})
    def clean(self):
        name = self.cleaned_data['name']
        if name[0].lower() != 's':
            raise ValidationError('The name 1st letter should start with s')