from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'posT':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messege={'success':"registration successful.please login"}
            return render(request, 'login.html',messege)
        else:
            messege = form.errors.as_text()
            return render(request, 'register.html',messege)

    return render(request,'register.html')

def login (request):
    return render(request,'login.html')