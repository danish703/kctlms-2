from django import forms
from .models import Course,Content

class CourseForm(forms.ModelForm):
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    hours = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Course
        fields = '__all__'


class ContentForm(forms.ModelForm):
    content_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    class Meta:
        model = Content
        exclude = ['course',]