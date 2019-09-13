from django import forms

class PhotoFrom(forms.Form):
    image = forms.ImageField()