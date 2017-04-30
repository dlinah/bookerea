"""bookerea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from siteapp import views
from siteapp.views.user import *
from siteapp.views.book import *
from siteapp.views.author import *
from siteapp.views.category import *
from siteapp.views.search_notif import *
from django.contrib.auth import views as auth_views
import notifications.urls as notif



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'siteapp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^register/$', signup, name='signup'),

    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^categorys/$', category.as_view(), name='categories'),
    url(r'^category/([0-9]+)/(.+)$', categoryBookList, name='category'),

    url(r'^books/$', BookList.as_view(),name='books'),
    url(r'^bookapi/$',BookUserApi.as_view()),
    url(r'^book/(?P<pk>[0-9]+)$', bookView,name='book'),

    url(r'^search/(.+)$', Search.as_view(), name='search'),
    url('^inbox/notifications/', include(notif, namespace='notifications'))
]
