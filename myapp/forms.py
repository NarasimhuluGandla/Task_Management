from .models import About
from django import forms

class Aboutform(forms.ModelForm):
    class Meta:
        model = About
        fields = ['name','contact','email','suggestions']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'contact':forms.TextInput(attrs={'placeholder':'Enter your contact'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your Mail Id'})
        }
        labels = {
            'contact':'PNO'
        }