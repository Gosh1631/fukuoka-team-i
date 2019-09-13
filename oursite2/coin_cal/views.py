from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Coin

class MoneyListView(ListView):
  model = Coin
  template_name= 'coin_cal/coin_cal_list.html'

def queryset(self):
  return money.objects.all()
def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        obj = Document.objects.all()
 
    return render(request, 'ai_image/model_form_upload.html', {
        'form': form,
        'obj': obj
    })