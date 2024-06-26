from django.shortcuts import render, redirect
from .forms import RegisterForm , LoginForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# # Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')  # Ensure you have a named URL for the login view
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')


def join_call(request):
    if request.method == 'POST':
        roomId = request.POST['roomID']
        return redirect('/meeting?roomID='+roomId)
    return render(request,'join_room.html')

@login_required
def video_call(request):
    return render(request, 'videocall.html',{'name':request.user.first_name})