from django.shortcuts import render,redirect
from .forms import LoginForm,SignUpForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             # Corrected the typo 'passowrd' to 'password'
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            
#             if user is not None:
#                 login(request, user)  # Log the user in
#                 return redirect('core:home')  # Redirect to home page on successful login
            
#     else:
#         form = LoginForm()  # Show an empty form if request is GET

#     return render(request, 'core/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Check if the user is authenticated and if admin
                print(f"User authenticated: {user}")  # Debugging line
                print(f"Is Admin: {user.is_staff}")  # Debugging line
                
                login(request, user)  # Log the user in
                return redirect('core:home')  # Redirect to home page on successful login
            else:
                print("Authentication failed.")  # Debugging line
        else:
            print("Form is not valid.")  # Debugging line

    else:
        form = LoginForm()  # Show an empty form if request is GET

    return render(request, 'core/login.html', {'form': form})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)  
            return redirect('core:login')  
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('core:login')  # Redirect to the login page after logout

def home_view(request):
    return render(request, 'core/home.html')