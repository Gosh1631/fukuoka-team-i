from django import forms
from .models import Document

class PhotoFrom(forms.Form):
    image = forms.ImageField()
class DocumentForm(form.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'photo')