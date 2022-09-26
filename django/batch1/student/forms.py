from django import forms
from django.forms.widgets import NumberInput
from .models import *
class RegModelForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields=('fname','lname','age','place')
class UserLogModelForm(forms.ModelForm):
    class Meta:
        model=UserLog
        exclude=('userid',)

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('emp_name','emp_age','salary','gender')

class UploadImageModelForm(forms.ModelForm):
    class Meta:
        model=UploadImage
        fields=('title','des','image')

class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model=UploadFile
        fields=('title','des','file')
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
gender=[
    ('m','Male'),
    ('f','Female'),
]
class RegForm(forms.Form):
    fname=forms.CharField()
    lname=forms.CharField()
    age=forms.IntegerField()
    dob=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    place=forms.CharField()
    address=forms.CharField(widget=forms.Textarea)
    email=forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':1}))
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=gender)
    colors=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    agree = forms.BooleanField()

