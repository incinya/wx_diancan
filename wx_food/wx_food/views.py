from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def main_view(request):
    items = {'items': [{
        'id_': 1,
        'title': '"折扣"湖南辣椒小炒肉1111',
        'price': 12,
        # active: 是否选中‘添加’按钮
        'active': False,
        'num': 1,
        'menuId': '精品家常菜',
        'bargin': "折扣"

    }, {
        'id_': 2,
        'title': '‘热销’湖南辣椒小炒肉',
        'price': 13,
        'active': False,
        'num': 1,
        'menuId': '精品家常菜',
        'all': '所有菜品'
    }, {
        'id_': 3,
        'title': '湖南辣椒小炒肉3',
        'price': 14,
        'active': False,
        'num': 1,
        'menuId': '精品家常菜'

    }, {
        'id_': 4,
        'title': '湖南辣椒小炒肉4',
        'price': 15,
        'active': False,
        'num': 1,
        'menuId': '精品家常菜'
    }, {
        'id_': 5,
        'title': '湖南辣椒小炒肉5',
        'price': 16,
        'active': False,
        'num': 1,
        'menuId': '精品家常菜'
    }, ], }
    return JsonResponse(items)


def index_view(request):
    return render(request, 'index.html', locals())


def test_view(request):
    with open('templates/index/detail/style/images/title_arrow.gif','rb') as f:
        data = f.read()
    return HttpResponse(data)
