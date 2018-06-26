# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test.objects.get(id=2)
    test1.name = 'Google'
    test1.save()

    Test.objects
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")