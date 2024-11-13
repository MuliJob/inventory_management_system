from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  title = 'Welcome: This is the Home Page'
  context = {
    'title': title,
  }
  return render(request, 'home.html', context)

@login_required
def list_items(request):
  header = 'List of Items'
  form = StockSearchForm(request.POST or None)
  queryset = Stock.objects.all()
  context = {
    'header': header,
    'queryset': queryset,
    'form': form
  }
  if request.method == 'POST':
    queryset = Stock.objects.filter(category__icontains=form['category'].value(),
                                    item_name__icontains=form['item_name'].value()
                                    )
    if form['export_to_CSV'].value() == True:
      response = HttpResponse(content_type='text/csv')
      response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
      writer = csv.writer(response)
      writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
      instance = queryset
      for stock in instance:
        writer.writerow([stock.category, stock.item_name, stock.quantity])
      return response
    context = {
      'form': form,
      'header': header,
      'queryset': queryset,
    }
  return render(request, 'list-items.html', context)

@login_required
def add_items(request):
  form = StockCreateForm(request.POST or None)
  if form.is_valid():
    form.save()
    messages.success(request, 'Successfully saved')
    return redirect('/list-items')
  context = {
    'form': form,
    'title': 'Add Item',
  }
  return render(request, 'add-items.html', context)

@login_required
def update_items(request, pk):
  queryset = Stock.objects.get(id=pk)
  form = StockUpdateForm(instance=queryset)
  if request.method == 'POST':
    form = StockUpdateForm(request.POST, instance=queryset)
    if form.is_valid():
      form.save()
      messages.success(request, 'Successfully saved')
      return redirect('/list-items')
  
  context = {
    'form': form
  }
  return render(request, 'add-items.html', context)

@login_required
def delete_items(request, pk):
  queryset = Stock.objects.get(id=pk)
  if request.method == 'POST':
    queryset.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('/list-items')
  return render(request, 'delete-items.html')

@login_required
def stock_detail(request, pk):
  queryset = Stock.objects.get(id=pk)
  context = {
    'queryset': queryset,
  }
  return render(request, 'stock-detail.html', context)

@login_required
def issue_items(request, pk):
  queryset = Stock.objects.get(id=pk)
  form = IssueForm(request.POST or None, instance=queryset)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.quantity -= instance.issue_quantity
    # instance.issue_by = str(request.user)
    messages.success(request, 'Issued SUCCESSFULLY. ' + str(instance.quantity) + ' ' + str(instance.item_name) + 's now left in Store')
    instance.save()

    return redirect('/stock-detail/'+str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())
  
  context = {
    'title': 'Issue ' + str(queryset.item_name),
    'queryset': queryset,
    'form': form,
    'username': 'Issue By: ' + str(request.user),
  }
  return render(request, 'add-items.html', context)

@login_required
def receive_items(request, pk):
  queryset = Stock.objects.get(id=pk)
  form = ReceiveForm(request.POST or None, instance=queryset)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.quantity += instance.receive_quantity
    instance.save()
    messages.success(request, 'Received SUCCESSFULLY. ' + str(instance.quantity) + ' ' + str(instance.item_name) + 's now in Store')


    return redirect('/stock-detail/'+str(instance.id))
    # return HttpResponseRedirect(instance.get_absolute_url())
  
  context = {
    'title': 'Receive ' + str(queryset.item_name),
    'instance': queryset,
    'form': form,
    'username': 'Received By: ' + str(request.user),
  }
  return render(request, 'add-items.html', context)

@login_required
def reorder_level(request, pk):
  queryset = Stock.objects.get(id=pk)
  form = ReorderLevelForm(request.POST or None, instance=queryset)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, 'Reorder level for ' + str(instance.item_name) + ' is updated to ' + str(instance.reorder_level))


    return redirect('/list-items')
  
  context = {
    'instance': queryset,
    'form': form,
  }
  return render(request, 'add-items.html', context)
