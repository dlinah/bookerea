from django.shortcuts import render

def home(req):
    return render(req, 'siteapp/home.html')
