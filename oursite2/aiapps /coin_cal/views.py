from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
  template = loader.get_template('coin_cal/index.html')
  context = {'form'}
  return HttpResponse("Hello World!")

def predict(request):
  return HttpResponse('Show result')