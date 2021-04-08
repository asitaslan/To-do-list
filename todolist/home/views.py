from django.contrib.auth import login, authenticate, logout

# Create your views here.
from home.forms import SignUpForm
from home.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from lists.models import Lists, ListForm


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



@login_required(login_url='/login')  # Check login
def lists(request):
    current_user = request.user
    lists = Lists.objects.filter(user_id=current_user)

    return render(request, 'index.html', lists)


@login_required(login_url='/login')  # Check login
def addlist(request):
    if request.method == 'POST':
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Lists()  # connetion with models
            data.user_id = current_user.id
            data.name = form.cleaned_data['name']
            data.slug = form.cleaned_data['slug']
            data.save()  # save to database
            messages.success(request, 'Your Content Insterted Successfuly')
            return HttpResponseRedirect('/')
        else:
            messages.success(request, 'Content Form Error:' + str(form.errors))
            return HttpResponseRedirect('/addlist')
    else:

        form = ListForm()
        context = {
            'form': form,
        }
        return render(request, 'addlist.html', context)