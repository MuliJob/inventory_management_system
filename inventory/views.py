from django.shortcuts import render
from .models import Stock

# Create your views here.
def home(request):
  title = 'Welcome: This is the Home Page'
  context = {
    'title': title,
  }
  return render(request, 'home.html', context)

def list_items(request):
  title = 'List of Items'
  queryset = Stock.objects.all()
  context = {
    'title': title,
    'queryset': queryset
  }
  return render(request, 'list-items.html', context)