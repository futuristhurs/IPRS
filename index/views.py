from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'home.html', context)

from django.shortcuts import render, redirect
from .forms import UserForm  # Make sure to import your form

# def register(request):
#     context = {
#         'title': 'Register'
#     }
    
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
        
#     else:
#         form = UserForm()
#     return render(request, 'register.html', context, {'form': form})
def register(request):
    page = 'register'
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')



    return render(request, 'register.html', {'form': form})
        

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
      login(request, user)
      # Redirect to the appropriate page after successful login
      return redirect('/home')  # Change this to your desired redirect URL
    else:
      # Login failed
      error_message = 'Invalid username or password.'
      context = {'error_message': error_message}
      return render(request, 'login.html', context)
  else:
    context = {}
    return render(request, 'login.html', context)

def logout(request):
  logout(request)
  # Redirect to the appropriate page after logout
  return redirect('/login')  # Change this to your desired redirect URL
