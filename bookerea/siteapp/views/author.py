from django.shortcuts import render,redirect
from ..models import Author
from django.views import View
from django.http import HttpResponse


class AuthorList(View):
    def get(self,request):
        authors = Author.objects.all()
        my_auth = None
        if request.user.is_authenticated():
            my_auth=request.user.authors.all().values()
            my_auth=list(map((lambda x: x['id']), my_auth))
            print('myauth',my_auth)
        return render(request, 'siteapp/authors.html', {'authors': authors,'my_auth':my_auth})
    def post(self,request):

        if request.user.is_authenticated():
            if request.POST['follow'] == '1':
                request.user.authors.add(request.POST['auth_id'])
                return HttpResponse(' follow success')
            else:
                request.user.authors.remove(request.POST['auth_id'])
                return HttpResponse(' unfollow success')
        else:
            return HttpResponse('you are not logged in')