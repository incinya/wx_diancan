from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from . import utils
from ServerApp import models
import json
from weixin import WXAPPAPI
from ServerApp import utils


@require_http_methods(["POST", "GET"])
def wechat_login(request):
    if request.method == "POST":
        received_data = json.loads(request.body.decode('utf-8'))
        code = received_data['code']
        # nickname = received_data['nickname']
        avatar = received_data['avatar']
        api = WXAPPAPI(appid='wx4ae96ebaaa93e809',
                       app_secret='4ff3aa9039ec5e2c5b3190f4297646b0')
        try:
            session_info = api.exchange_code_for_session_key(code=code)
            open_id = session_info['openid']
            # Check whether first log in
            queryset = models.NormalUser.objects.filter(open_id=open_id)
            if queryset.exists():
                # Not first log in, refresh nickname and avator
                user = queryset.first()
                # user.nickname = nickname
                user.avatar = avatar
                user.save()
            else:
                user = models.NormalUser(open_id=open_id, avatar=avatar)
                user.save()
            request.session[utils.BUYER_USERNAME] = user.pk
            return HttpResponse('Log In Success!', status=200)
        except Exception as err:
            print(err)
            return HttpResponse('Wechat Log In Fail!', status=500)

    if request.method == "GET":
        if utils.BUYER_USERNAME in request.session:
            # Logged In
            login = True
        else:
            login = False
        return utils.eatDDJsonResponse({"login": login})
