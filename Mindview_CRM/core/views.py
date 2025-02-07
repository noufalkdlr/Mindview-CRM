from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:   
                login(request, user)

                if user.is_superuser:
                    return redirect('core:dashboard')
                else:
                    return redirect('core:home')

    else:
        form = LoginForm() 

    return render(request, 'core/login.html', {'form': form})

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def dashboard_view(request):
    return render(request, 'core/dashboard.html')






def logout_view(request):
    logout(request)     
    return redirect('core:login') 

def home_view(request):
    return render(request, 'core/home.html')