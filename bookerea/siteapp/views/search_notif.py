from ..models import Book_user,Book
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.decorators.http import require_GET
import json
from django.conf import settings
from pusher import Pusher

class PusherMixin(object):

    def render_to_response(self, context, **response_kwargs):
        channel = u"new_book"
        event_data = {'user': self.request.user.username}
        pusher = Pusher(app_id=settings.PUSHER_APP_ID,
                        key=settings.PUSHER_KEY,
                        secret=settings.PUSHER_SECRET)
        pusher.trigger(
            [channel, ],
            self.pusher_event_name,
            event_data
        )

        return super(PusherMixin, self).render_to_response(context, **response_kwargs)

    def __object_to_json_serializable(self, object):
        model_dict = model_to_dict(object)
        json_data = json.dumps(model_dict, cls=DjangoJSONEncoder)
        data = json.loads(json_data)
        return data


class Search(View):
    def get(self,request,*args):
        key=args[0]
        books=Book.objects.filter(title__contains=key).values()
        result=list(map((lambda x: {'id':x['id'],'title':x['title']}), books))
        return JsonResponse(result,safe=False)




