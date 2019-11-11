from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import json
from ServerApp import models
from .auth_required_decorator import eatdd_login_required
from . import utils


@require_http_methods(["GET", "PUT"])
@eatdd_login_required
def manage_restaurant(request, restaurantId):
    username = request.session['username']
    if request.method == "GET":
        queryset = models.Restaurant.objects.filter(pk=restaurantId)
        if queryset.exists():
            return utils.eatDDJsonResponse(restaurant_to_dict(queryset.first()))
        else:
            return HttpResponse('fail', status=400)

    elif request.method == "PUT":
        pass


@require_http_methods(["POST"])
@eatdd_login_required
def create_restaurant(request):
    username = request.session['username']

    if request.method == "POST":
        received_data = json.loads(request.body.decode('utf-8'))
        newRestaurant = models.Restaurant(name=received_data['name'],
                                          description=received_data['description'],
                                          image=received_data['image_url'],
                                          boss=models.BusinessUser.objects.get(username=username))

        if not models.Restaurant.objects.filter(name=newRestaurant.name).exists():
            newRestaurant.save(force_insert=True)
            return utils.eatDDJsonResponse(restaurant_to_dict(newRestaurant))
        else:
            return HttpResponse('fail', status=400)


@require_http_methods(["GET"])
@eatdd_login_required
def get_all_restaurant(request):
    username = request.session[utils.BOSS_USERNAME]
    queryset = models.Restaurant.objects.filter(boss__username=username)
    return utils.eatDDJsonResponse({"restaurants": restaurant_queryset_to_array(queryset)})


def restaurant_queryset_to_array(queryset):
    restaurants = []
    for item in queryset:
        restaurants.append(restaurant_to_dict(item))
    return restaurants


def restaurant_to_dict(item):
    return {
        "id": item.pk,
        "name": item.name,
        "description": item.description,
        "image": item.image
    }
