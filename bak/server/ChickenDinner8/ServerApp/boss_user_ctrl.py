from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
import json
from ServerApp import models
import hashlib

@require_http_methods(["GET", "POST", "PUT"])
def bossUserAdmin(request):
    # Create a user
    if request.method == "POST":
        received_data = json.loads(request.body)
        # print (received_data)

        newUser = models.BusinessUser(username=received_data['username'], password=addSalt(received_data['password']))

        if not models.BusinessUser.objects.filter(username=newUser.username).exists():
            newUser.save(force_insert=True)
            return HttpResponse("Regist new user successfully!")
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

def addSalt(data):
    for i in range(10):
        data = (hashlib.md5((data + "eatDD").encode('utf-8')).hexdigest())
    return data
