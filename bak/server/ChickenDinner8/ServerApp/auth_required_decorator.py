from django.http import HttpResponse
from ServerApp import utils

'''
Personlized require_login decorator
'''


def eatdd_login_required(func):
    def check_login_status(request, *args, **kwargs):
        if utils.BOSS_USERNAME in request.session or utils.BUYER_USERNAME in request.session:
            # Already Log In
            return func(request, *args, **kwargs)
        else:
            # Not Log In
            return HttpResponse("Not Log In", status=401)

    return check_login_status
