from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User


from .forms import  NewUserForm


UserModel = get_user_model()

def get_complete_name(request):
    if request.user.get_short_name():
        un = request.user.get_short_name()
        print(un)
        if request.user.get_full_name():
            un = request.user.get_full_name()
            print(un)
    
    else:
        un = request.user.username
        print(un)
            
    return un

# Create your views here.
def home(request):
    un = ''
    if request.user.is_authenticated:
        un = get_complete_name(request)
        
    sitename = 'karmasite'
    return render( request, 'home/home.html', {"sitename": sitename, "un" : un })



@login_required
def account_settings(request):
    return render( request, 'home/account.html', {'name': get_complete_name(request)})
    
    
def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data.get("username"), 
                email = form.cleaned_data.get("email"), 
                password = form.cleaned_data.get("password1")
            )
            user.save()
            messages.success(request, "New user created.")
            
        else:
            messages.error(request, "Invalid form.")
        
        return HttpResponseRedirect(' ')

    else:
        form = NewUserForm()

    return render(request, "home/signup.html", {"form": form})

    