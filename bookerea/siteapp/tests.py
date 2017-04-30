import datetime
from django.test import TestCase
from .models import *
from django.urls import reverse


class testest(TestCase):

    def test_search(self):
        response= self.client.get('/search/mm')
        self.assertEqual(response.status_code, 200)
    def test_book(self):
        response= self.client.get('/bookapi')
        print(dict(response))
        self.assertEqual(response.status_code, 200)
        response= self.client.post('/bookapi',{'id':1})
        self.assertEqual(response.status_code, 200)

