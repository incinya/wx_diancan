from django.http import HttpResponse
import decimal
import simplejson as json

BOSS_USERNAME = 'username'
BUYER_USERNAME = 'buyer_username'


def eatDDJsonResponse(obj):
    return HttpResponse(json.dumps(obj, use_decimal=True), content_type="application/json")
