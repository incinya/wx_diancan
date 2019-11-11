from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
import json
from . import models


@require_http_methods(["GET", "POST", "DELETE"])
def login(request):
    received_data = json.loads(request.body.decode('utf-8'))

    if request.method == 'POST':
        queryset = models.BusinessUser.objects.filter(username=received_data['username'],
                                                      password=received_data['password'])
        if queryset.exists():
            user = queryset.first()
            request.session['username'] = user.username
            return HttpResponse('Log In')
        else:
            return HttpResponse('Error LogIn', status=400)


@require_http_methods(["GET", "POST", "PUT"])
def bossUserAdmin(request):
    # Create a user
    if request.method == "POST":
        received_data = json.loads(request.body)
        # print (received_data)

        newUser = models.BusinessUser(username=received_data['username'], password=received_data['password'])

        if not models.BusinessUser.objects.filter(username=newUser.username).exists():
            newUser.save(force_insert=True)
            return HttpResponse("Regist new user successful!")
        else:
            return HttpResponse("Duplicate Username", status=400)

    elif request.method == "GET":
        username = request.session['username']
        queryset = models.BusinessUser.objects.filter(username=username)

        if queryset.exists():
            return HttpResponse(username)
        else:
            return HttpResponse("Not Log In", status=400)

    elif request.method == "PUT":
        pass


@require_http_methods(["GET", "POST", "PUT"])
def req_restaurant(request):
    username = request.session['username']

    if request.method == "POST":
        received_data = json.loads(request.body.decode('utf-8'))
        newRestaurant = models.Restaurant(name=received_data['name'],
                                          description=received_data['description'],
                                          image=received_data['image_url'],
                                          boss=models.BusinessUser.objects.get(username=username))

        if not models.Restaurant.objects.filter(name=newRestaurant.name).exists():
            newRestaurant.save(force_insert=True)
            return HttpResponse("Regist new restaurant successful!")
        else:
            return HttpResponse('fail', status=400)

    elif request.method == "GET":
        queryset = models.Restaurant.objects.filter(username=username)
        if queryset.exists():
            return HttpResponse(queryset.first())
        else:
            return HttpResponse('fail', status=400)

    elif request.method == "PUT":
        pass


def sendJsonData(msg, status_code=200):
    return HttpResponse(msg, content_type="application/json", status=status_code)
