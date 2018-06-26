"""twodj URL Configuration

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
from django.conf.urls import url

from django.contrib import admin
from twodj import views, testdb, search, search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'data/(?P<id>\d+)/$', views.data),
    url(r'update', views.update),
    url(r'index', views.index),
    url(r'hello', views.hello),
    url(r'home', views.home, name='hemo'),
    url(r'zhaobing', views.zhaobing, name='zhaobing'),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),

]
