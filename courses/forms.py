from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',}))
    hours = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Course
        exclude = '__all__'