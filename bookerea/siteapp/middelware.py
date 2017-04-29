from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages
from django.shortcuts import render,redirect


class Authin(MiddlewareMixin):
    def process_request(self,request):
        if request.user.is_authenticated():
            return None
        else:
            messages.info(request, 'please log in first')
            return None

