from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm

# Create your views here.
def index(request):
    #return HttpResponse('<h1>INVENTORY MANAGEMENT SYSTEM</h1>')
    return render(request,'Inventory/index.html')
def register(request):
    if (request.method=="POST"):
        print("Entered")
        form=NewUserForm(request.POST)
        print(form)
        print(request.POST)
        if form.is_valid():
        
            form.save(True)
    form=NewUserForm
    context={"register_form":form}
    return render(request,'Inventory/register.html',context)
