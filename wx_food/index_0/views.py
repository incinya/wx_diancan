from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Menu
from django.views.generic import View
import base64


# Create your views here.
def index_view(request):
    """
    主路由逻辑处理
    前端模板传过来的URL所有请求全是get  /index开头...
    """
    res = request.META.get('PATH_INFO')
    if res == '/index/':
        # 返回主页
        return render(request, 'index.html', locals())
    res = res[1:]

    # 由于修改请求有查询字符串,作如下处理
    if res.find(r'updateFood.html') != -1 and res.find(r'style') == -1:
        id = request.GET.get('id')
        dict01 = Filter().get(request)
        for item in dict01['items']:
            if str(item['id']) == id:
                return render(request, 'index/detail/updateFood.html', locals())

    if res.endswith('.html'):
        # 遇到模板请求,返回模板
        dict01 = Filter().get(request)
        return render(request, res, locals())

    # 静态资源请求返回静态文件
    with open(res, 'rb') as f:
        data = f.read()
    return HttpResponse(data)


class Add(View):
    def get(self, request, title, price, menuId, img_data):
        dict01 = Filter().get(request)
        if dict01['items']:
            id = dict01['items'][-1]['id'] + 1
        else:
            id = 1
        # Menu.objects.create(
        #     id_=id,
        #     title=title,
        #     price=price,
        #     num=1,
        #     menuId=menuId,
        # )
        obj = Menu(id_=id, title=title, price=price, num=1, menuId=menuId)
        obj.img.put(img_data, content_type='image/jpeg')
        obj.save()
        return HttpResponse('hello world')


class Filter(View):
    def get(self, request):
        res = Menu.objects.filter()
        """
        items = {'items': [{
            'id': 1,
            'title': '"折扣"湖南辣椒小炒肉1111',
            'price': 12,
            # active: 是否选中‘添加’按钮
            'active': False,
            'num': 1,
            'menuId': '精品家常菜',
            'bargin': "折扣"
        }]}"""
        dict01 = {'items': []}
        dict02 = {}
        for item in res:
            dict02['id'] = item.id_
            dict02['title'] = item.title
            dict02['price'] = item.price
            dict02['active'] = item.active
            dict02['num'] = item.num
            dict02['menuId'] = item.menuId
            dict02['bargin'] = item.bargin
            dict02['img'] = item.img.read()
            dict01['items'].append(dict02)

            dict02 = {}

        def take_id(elem):
            return elem['id']
        
        dict01['items'].sort(key=take_id)

        # print(dict01['items'][-1]['id']) # 最后一项数据的id
        return dict01
        # return JsonResponse(dict01)


class Update(View):
    def get(self, request, title, price, menuId, img, id=0):
        Menu().update(id_=id, title=title, price=price, num=1, menuId=menuId)
        Del().get(request, id)
        obj = Menu(id_=id, title=title, price=price, num=1, menuId=menuId)
        obj.img.put(img, content_type='image/jpeg')
        obj.save()
        return HttpResponse('hello world')


class Del(View):
    def get(self, request, id=0):
        Menu.objects.filter(id_=id).first().delete()
        return


def food_view(request):
    id = request.GET.get("id")
    method = request.GET.get("method")
    if method == "delete":
        Del().get(request, id=id)
        dict01 = Filter().get(request)
        return render(request, 'index/detail/foodList.html', locals())


def addfood_view(request):
    """
    <QueryDict: {'cid': ['1'], 'id': [''], 'foodName': ['油酥鸭'],
     'price': ['998'], 'mprice': ['404'], 'introduce': ['hello'], 'imageUrl': ['']}>
    """
    kind = {'1': "特色小龙虾", '2': "精品家常菜", '3': "干锅系列", '4': '炒饭系列'}
    title = request.POST.get('foodName')
    price = request.POST.get('price')
    introduce = request.POST.get('introduce')
    image = request.FILES.get('image')
    menuId = None
    with open('./index_0/media/item-m.jpg', 'rb') as f:
        img_data = f.read()
        img_data = b'data:image/png;base64,' + base64.b64encode(img_data)
    if request.POST.get('cid'):
        menuId = kind[request.POST.get('cid')]

    if image:
        img_data = b'data:image/png;base64,'
        for line in image.chunks():
            img_data += base64.b64encode(line)

    if title and price and menuId:

        Add().get(request, title, price, menuId, img_data)
        msg = f'{title}添加成功!!!!'
    else:
        msg = '菜品添加失败'
    if request.method == 'GET':
        msg = ""

    return render(request, 'index/detail/saveFood.html', locals())


def updatefood_view(request):
    kind = {'1': "特色小龙虾", '2': "精品家常菜", '3': "干锅系列", '4': '炒饭系列'}
    if request.META['REQUEST_METHOD'] == 'GET':
        return index_view(request)
    id = request.POST.get('id')

    cid = kind[request.POST.get('cid')]
    foodname = request.POST.get('foodName')
    price = request.POST.get('price')
    img = request.POST.get('image').encode()
    image = request.FILES.get('imageUrl')

    if image:
        img = b'data:image/png;base64,'
        for line in image.chunks():
            img += base64.b64encode(line)

    Update().get(request, foodname, price, cid, img, id=id)
    return HttpResponse("菜品修改成功!!")


def main_view(request):
    res = Menu.objects.filter()

    """
    items = {'items': [{
        'id': 1,
        'title': '"折扣"湖南辣椒小炒肉1111',
        'price': 12,
        # active: 是否选中‘添加’按钮
        'active': False,
        'num': 1,
        'menuId': '精品家常菜',
        'bargin': "折扣"
    }]}"""
    dict01 = {'items': []}
    dict02 = {}
    for item in res:
        dict02['id'] = item.id_
        dict02['title'] = item.title
        dict02['price'] = item.price
        dict02['active'] = item.active
        dict02['num'] = item.num
        dict02['menuId'] = item.menuId
        dict02['bargin'] = item.bargin
        dict02['img'] = item.img.read().decode()
        dict01['items'].append(dict02)
        dict02 = {}

    # print(dict01['items'][-1]['id']) # 最后一项数据的id
    # return dict01
    return JsonResponse(dict01)


def init_view(request):
    img = 'data:image/png;base64,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'
    img = img.encode()
    for i in range(3):
        Add().get(request, f'精品奥特曼{i}', 998, '精品家常菜', img)
    return HttpResponse('hello world')
