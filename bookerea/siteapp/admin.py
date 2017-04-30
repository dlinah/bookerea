from django.contrib import admin
from .models import Book,Author,Category,User
from django.db import models
from notifications.signals import notify

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)

user_admin=User.objects.filter(id=1).values()[0]
users=User.objects.all().values()


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     def response_add(self,request,obj,post_url_continue=None):
#         print('inadminnnnnnnnnnnnnnn')
#         print(obj.id)
#         data={'id':obj.id,'title':obj.title,'author':obj.author.name}
#
#         notify.send(
#                     users,
#                     'new_book',data
#
#                     )
#         res=super(BookAdmin, self).response_add(request,obj)
#         return res

