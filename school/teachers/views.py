from django.shortcuts import render
#from django import forms
from .form import TeacherForm
# Create your views here.
#class TeacherForm(forms.Form):
#    name = forms.CharField(max_length=15)

def form_view(request):
    if request.method == 'POST':
        #print(request.POST)
        form = TeacherForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            cd['name']
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher.html', {'form':form})