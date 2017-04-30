from ..models import Book_user,Book
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.http import require_GET




class BookList(View):

    def get(self,request):
        recommended=None
        books=Book.objects.all().order_by('-id')[:100]
        books=populate_book(request,books)
        recent_books=books[:10]
        popular=order_by_rating(books)
        if request.user.is_authenticated():
            fcat=request.user.categories.all().values()
            fcat=list(map((lambda x: x['id']), fcat))
            fauthor=request.user.authors.all().values()
            fauthor=list(map((lambda x: x['id']), fauthor))
            print(fcat,fauthor)
            recommended=Book.objects.filter(Q(author_id__in=fauthor) | Q(category_id__in=fcat))
            recommended=populate_book(request,recommended)
        return render(request,'siteapp/book_list.html',{'recent':recent_books,'popular':popular,'recommended':recommended })


def order_by_rating(books):
    b=list(books)
    b.sort(key=lambda x: x.rating, reverse=True)
    return b


def populate_book(request,books):
    if request.user.is_authenticated():
        for book in books:
            book.rating(request.user)
            book.get_user_mark(request.user)
    else:
        for book in books:
            book.rating(0)
    return books


@require_GET
def bookView(request, pk):
    books = Book.objects.filter(id=pk)
    books = populate_book(request,books)
    return render(request, 'siteapp/book.html', {'book': books[0]})


class BookUserApi(View):
    def post(self, request):
        if request.user.is_authenticated():
            P=request.POST
            if Book_user.objects.filter(book_id=P['book_id'],user_id=request.user.id).exists():
                item = Book_user.objects.get(book_id=P['book_id'], user_id=request.user.id)
                if 'mark_as' in P:
                    item.mark_as=P['mark_as']
                if 'rating' in P:
                    item.rating=P['rating']
                item.save()
            else:
                if 'mark_as' in P:
                    Book_user.objects.create(book_id=P['book_id'], user_id=request.user.id ,mark_as=P['mark_as'])
                elif 'rating' in P:
                    Book_user.objects.create(book_id=P['book_id'], user_id=request.user.id,rating=P['rating'])
                elif 'rating' in P and 'mark_as' in P:
                    Book_user.objects.create(book_id=P['book_id'], user_id=request.user.id ,mark_as=P['mark_as'] ,rating=P['rating'])

            return HttpResponse('success')

        else:
            messages.info(request, 'please log in first to')
            return HttpResponse('you are not logged in')