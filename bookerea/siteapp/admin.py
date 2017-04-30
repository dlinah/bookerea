from django.contrib import admin
from .models import Book,Author,Category,User
from django.db import models
from notifications.signals import notify
from django.contrib.auth.models import Group

admin.site.register(Author)
admin.site.register(Category)




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def response_add(self,request,obj,post_url_continue=None):
        self.user_admin = User.objects.get(id=1)
        self.group = Group.objects.get(id=1)
        print('inadminnnnnnnnnnnnnnn')
        print(obj.id)
        data={'id':obj.id,'title':obj.title,'author':obj.author.name}
        notify.send(self.user_admin, recipient=self.group, verb='new book', action_object=self.user_admin,data=data)
        res=super(BookAdmin, self).response_add(request,obj)
        return res

