from django.db import models
from django.contrib.auth.models import AbstractUser
import json
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.db.models import Avg
from django.shortcuts import get_object_or_404, get_list_or_404

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category')
    desc=models.TextField(blank=True,max_length=500)
    cover=models.ImageField(upload_to = 'books' , default = 'books/no-img.jpg')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publish_date=models.DateField(blank=True,null=True)
    # users = models.ManyToManyField(
    #     User,
    #     through='Book_user',
    #     through_fields=('book', 'user'),
    # )

    def rating(self,user):
        if user != 0 :
            try:
                self.rating = Book_user.objects.get(book=self,user=user).rating
            except:
                try:
                    self.rating = Book_user.objects.filter(book=self).aggregate(Avg('rating'))['rating__avg']
                except:
                    print('no rating for book' + str(self.id))

        else:
            try:
                self.rating = Book_user.objects.filter(book=self).aggregate(Avg('rating'))['rating__avg']
            except:
                print('no rating for book'+str(self.id))
        if self.rating == None:
            self.rating=0.0
    def get_user_mark(self,user):
        try:
             self.mark_as= Book_user.objects.get(book=self,user=user).get_mark_as_display
        except:
            print('no mark for book'+str(self.id))
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('books')

class Author(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to = 'authors' , default = 'authors/no-img.jpg')
    bio=models.TextField(blank=True,max_length=500)
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)

class User(AbstractUser):
    image=models.ImageField(upload_to = 'users' , default = 'users/no-img.jpg')
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    books = models.ManyToManyField(Book, through='Book_user', through_fields=('user', 'book'),)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

class Book_user(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.FloatField(
    validators = [MinValueValidator(0), MaxValueValidator(4)],null=True)
    MARK_AS_CHOICES =(('w','wish list'),('c','currently reading'),('f','finished'))
    mark_as=models.CharField(max_length=2,choices=MARK_AS_CHOICES,default='')