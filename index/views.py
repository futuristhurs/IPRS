from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    context = {
        'title': 'Home Page'
    }
    return render(request, 'home.html', context)

def register(request):
    context = {
        'title': 'Register'
    }
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context, {'form': form})
        