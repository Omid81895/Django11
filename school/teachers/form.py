from django import forms

class TeacherForm(forms.Form):
    name = forms.CharField(label='your name', label_suffix='=', max_length=25, widget=forms.TextInput({'class':'form-control'}))
    email = forms.EmailField(help_text='your email should gmail account', required=True, error_messages={'required': 'please enter your email'})