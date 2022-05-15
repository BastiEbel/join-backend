from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from joinboard.models import Task


@login_required(login_url='/login')
# Create your views here.
def index(request):
    """
    this function create the JSON
    """
    if request.method == 'POST':
        Task.objects.create(text=request.POST['textvalue'], user=request.user, created_at=request.POST['datevalue'], description=request.POST['description'], category=request.POST['category'])
    return render(request, 'join/index.html')


def allTask(request):
    """
    this function returns the completely JSON
    """
    if request.method == 'GET':
        alljson = Task.objects.all()
        serialized_obj = serializers.serialize('json',  alljson, )
        return HttpResponse(serialized_obj[1:-1], content_type="application/json")


def singlejson(request, id):
    """
    this function returns the single JSON
    """
    if request.method == 'GET':
        single_json = Task.objects.get(id=id)
        serialized_obj = serializers.serialize('json', [ single_json, ])
        return HttpResponse(serialized_obj[1:-1], content_type="application/json")

def login_view(request):
    """
    This function is for the login. If the user exist or not
    """
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword' : True, 'wrongUsername' : True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})

def register_view(request):
    """
    This function is for the registration. It create the User.
    """
    redirect = request.POST.get('next', '/')
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('confirm_password'):
            user = User.objects.create_user(username=request.POST('username'), first_name=request.POST('first_name'), last_name=request.POST('last_name'), 
            email=request.POST('email'), password=request.POST('password'))
            user.save()
            return HttpResponseRedirect(redirect)
        else:
            return render(request, 'auth/register.html', {'wrongPassword': True})
    return render(request, 'auth/register.html')

def logout_view(request):
    """
    This function is for the Logout. It cancel the connection to the app.
    """
    redirect = request.POST.get('next', '/')
    auth_logout(request)
    return HttpResponseRedirect(redirect)