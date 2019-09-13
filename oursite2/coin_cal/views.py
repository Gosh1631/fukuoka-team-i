from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Coin

class MoneyListView(ListView):
  model = Coin
  template_name= 'coin_cal/coin_cal_list.html'

def queryset(self):
  return money.objects.all()
