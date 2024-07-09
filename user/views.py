from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.



def home(request):
    return render(request, 'home.html', {})
    

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in successfully"))
            return redirect('home')
        else:
            messages.success(request, ("There is an error"))
            return redirect('login')
      
    else:
        return render(request, 'login_user.html', {})
    
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('home')
    
              
    
    