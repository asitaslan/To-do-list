from django.shortcuts import render

from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# Create your views here.
# Create your views here.
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