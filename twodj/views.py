from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json

USER_LIST = []

# -*-coding:utf-8-*-
import json
import random
import time
from threading import Timer

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html', )


def home(request):
    return render(request, 'home.html', )


def zhaobing(request):
    return render(request, 'zhaobing.html', {})


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


#
# def home(request):
#     if request.method == 'GET':
#         return render_to_response('home.html', )
#     else:
#         u = request.POST.get('username')
#         s = request.POST.get('sex')
#         a = request.POST.get('age')
#         tem = {'username': u, 'sex': s, 'age': a}
#         USER_LIST.append(tem)
#         # return HttpResponse('username=' + u + "&password=" + s)
#         return render_to_response('home.html',
#                                   {'user_list': USER_LIST},
#                                   )


def data(request, id):
    rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
    rlist2 = []
    rlist2.append({"name": rlist[int(id)][0], "subject": rlist[int(id)][1]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response


def update(request):
    return render_to_response('update.html')
