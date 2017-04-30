from django.shortcuts import render,redirect
from ..models import Category,Book
from django.views import View
from django.http import HttpResponse
from django.views.decorators.http import require_GET



class category(View):
    def get(self,request):
        cat = Category.objects.all()
        mycat=None
        if request.user.is_authenticated():
            mycat=request.user.categories.all().values()
            mycat=list(map((lambda x: x['id']), mycat))
            print(mycat)
        return render(request, 'siteapp/categories.html', {'cat': cat,'mycat':mycat})
    def post(self,request):
        if request.user.is_authenticated():
            if request.POST['follow'] == '1':
                request.user.categories.add(request.POST['cat_id'])
                return HttpResponse(' follow success')
            else:
                request.user.categories.remove(request.POST['cat_id'])
                return HttpResponse(' unfollow success')
        else:
            return HttpResponse('you are not logged in')

@require_GET
def categoryBookList(request,*args):
    books=Book.objects.filter(category_id=args[0])
    return render(request, 'siteapp/category.html', {'books':books,'name':args[1] })

