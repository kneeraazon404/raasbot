from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import (
    ScrapedUser,
    Bot,
    LogData,
    User
)

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'core/index-admin.html', {
                'data': [
                    {
                        'name': str(user.user),
                        'bots_alive': Bot.objects.filter(user=user, is_alive=True).count(),
                        'users_scraped': ScrapedUser.objects.filter(user=user).count(),
                        'received_dm': LogData.objects.filter(user=user).count(),
                        'successful_dm': LogData.objects.filter(user=user, success=True).count(),
                        'unsuccessful_dm': LogData.objects.filter(user=user, success=False).count()
                    } for user in User.objects.all()
                ]
            })
        else:
            user = request.user.user
            print(user)
            return render(request, 'core/index.html', {
                'bots_alive': Bot.objects.filter(user=user, is_alive=True).count(),
                'users_scraped': ScrapedUser.objects.filter(user=user).count(),
                'received_dm': LogData.objects.filter(user=user).count(),
                'successful_dm': LogData.objects.filter(user=user, success=True).count(),
                'unsuccessful_dm': LogData.objects.filter(user=user, success=False).count()
            })
    else:
        return redirect(reverse('core:login_view'))

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('core:index'))
    if request.method == 'GET':
        return render(request, 'core/login.html')

    token = request.POST.get('token')

    user = authenticate(request, token=token)


    if user is not None:
        login(request, user)
        return redirect(reverse('core:index'))
    else:
        return HttpResponse('Unauthorized', status=500)

def dahsboard(request):
    return HttpResponse("Hello")

def logout_view(request):
    logout(request)
    return redirect(reverse('core:index'))
