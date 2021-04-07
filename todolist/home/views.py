from django.shortcuts import render

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect

# Create your views here.
from home.forms import SignUpForm
from home.models import UserProfile


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Warning! Check username or password")
            return HttpResponseRedirect('/login')
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Welcome... Registering is successfuly.")
            return HttpResponseRedirect('/')

    form = SignUpForm()
    context ={
        'form': form
    }
    return render(request, 'signup.html', context)