from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'posT':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'login.html',{'success':"registration successful.please login"})
        else:
            error_messege = form.errors.as_text()
            return render(request, 'register.html',{'success':error_messege})

    return render(request,'register.html')

def login (request):
    return render(request,'login.html')