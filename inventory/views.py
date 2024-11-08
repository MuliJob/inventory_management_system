from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockCreateForm

# Create your views here.
def home(request):
  title = 'Welcome: This is the Home Page'
  context = {
    'title': title,
  }
  return render(request, 'home.html', context)

def list_items(request):
  header = 'List of Items'
  queryset = Stock.objects.all()
  context = {
    'header': header,
    'queryset': queryset
  }
  return render(request, 'list-items.html', context)

def add_items(request):
  form = StockCreateForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('/list-items')
  context = {
    'form': form,
    'title': 'Add Item',
  }
  return render(request, 'add-items.html', context)