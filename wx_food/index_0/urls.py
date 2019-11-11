"""wx_food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import Add
from .views import Filter
from .views import Update
from .views import Del


from . import views

urlpatterns = [
    url(r'^add', Add.as_view()),
    url(r'^filter', Filter.as_view()),
    url(r'^update', Update.as_view()),
    url(r'^delete', Del.as_view()),

    url(r'detail/saveFood',views.addfood_view),
    url(r'detail/updateFood',views.updatefood_view),
    url(r'^wirelessplatform/food', views.food_view),

    url(r'^init', views.init_view),
    url(r'^main', views.main_view),


    url(r'',views.index_view),



]
