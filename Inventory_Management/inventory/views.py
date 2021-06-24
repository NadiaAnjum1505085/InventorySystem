from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('<h1>INVENTORY MANAGEMENT SYSTEM</h1>')
    return render(request,'Inventory/index.html')
def register(request):
    #return HttpResponse('<h1>INVENTORY MANAGEMENT SYSTEM</h1>')
    return render(request,'Inventory/register.html')