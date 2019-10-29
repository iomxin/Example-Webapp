from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect

def index(request) :
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            allItems = List.objects.all
            return render(request,'index.html',{'all':allItems})
    else:
        allItems = List.objects.all
        return render(request,'index.html',{'all': allItems})
def about(request) :
    today = datetime.datetime.now().date()
    return render(request,'about.html',{"today": today})
def contact(request) :
    today = datetime.datetime.now().date()
    return render(request,'contact.html',{"today": today})

def delete(request,itemID):
        items = List.objects.get(pk=itemID)
        items.delete()
        return redirect('index')

def crossout(request,itemID) :
        f=List.objects.get(pk=itemID)
        f.finished = True
        f.save()
        return redirect('index')

def uncross(request,itemID) :
        f=List.objects.get(pk=itemID)
        f.finished = False
        f.save()
        return redirect('index')

