from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
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

def login(request):
    forms = NewUserForm()
    if request.method == 'POST':
        forms = NewUserForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                #return redirect('dashboard')
    context = {'form': forms}
    #return render(request, 'users/login.html', context)
    

    return render(request,'Inventory/login.html')

