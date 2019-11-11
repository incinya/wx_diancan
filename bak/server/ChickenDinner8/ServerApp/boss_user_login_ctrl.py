from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
import json
from ServerApp import models
from .boss_user_ctrl import addSalt


@require_http_methods(["GET", "POST", "DELETE"])
def login(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        queryset = models.BusinessUser.objects.filter(username=received_data['username'],
                                                      password=addSalt(received_data['password']))
        if queryset.exists():
            user = queryset.first()
            request.session['username'] = user.username
            return HttpResponse('Log In')
        else:
            return HttpResponse('Error LogIn', status=400)

    if request.method == 'GET':
        if 'username' not in request.session:
            return HttpResponse('Not Log In', status=400)
        else:
            return HttpResponse(request.session['username'])

    if request.method == 'DELETE':
        if 'username' not in request.session:
            return HttpResponse('Not Log In', status=400)
        else:
            del request.session['username']
            return HttpResponse('Logged Out', status=200)
