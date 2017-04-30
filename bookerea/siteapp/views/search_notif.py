from ..models import Book_user,Book
from django.views import View
from django.http import HttpResponse,JsonResponse

class Search(View):
    def get(self,request,*args):
        key=args[0]
        books=Book.objects.filter(title__contains=key).values()
        result=list(map((lambda x: {'id':x['id'],'title':x['title']}), books))
        return JsonResponse(result,safe=False)




