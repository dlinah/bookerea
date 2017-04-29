import datetime
from django.utils import timezone
from django.test import TestCase
from .models import *
from django.urls import reverse


class testest(TestCase):

    def test_1(self):
        response= self.client.get(reverse('book'))
        print('intest')
        self.assertEqual(response.status_code, 200)
        # self.assertIs(future_question.was_published_recently(), False)
