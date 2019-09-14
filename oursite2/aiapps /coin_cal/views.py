from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Photoform 
# Create your views here.
def index(request):
  template = loader.get_template('coin_cal/index.html')
  context = {'form':PhotoForm()}
  return HttpResponse(tempate.render(context, request))

def predict(request):
  if not request.method == 'Post'
    return
    redirect('coin_cal:index')

  form = PhotoForm(request.Post, request.FILES)
  if not form.is_valid():
    raise ValueError('Formが不正です')

  photo = Photo(image=form.cleaned_data[''])

  return HttpResponse()