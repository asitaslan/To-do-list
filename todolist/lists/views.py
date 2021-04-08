from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from lists.models import Lists


@login_required(login_url='/login')  # Check login
def lists(request):
    current_user = request.user
    list = Lists.objects.filter(user_id=current_user.id)
    context = {
        'lists': list,
    }
    return render(request, 'index.html', context)