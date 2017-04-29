from django.shortcuts import render,redirect
from ..models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


CATEGORIES=('Science fiction',
'Satire',
'Drama',
'Action and Adventure',
'Romance',
'Mystery',
'Horror',
'Self help')

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('image','username', 'email','password1', 'password2', )

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            print('vaaaaaaaaaaaalid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'siteapp/register.html', {'form': form})

class follow(View):
    def get(self,request):
        pass
    def post(self,request):
        pass