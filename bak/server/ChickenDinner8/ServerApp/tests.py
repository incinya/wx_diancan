from django.test import TestCase
from ServerApp.models import Menu, Order
from datetime import datetime


# Create your tests here.
class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(foodName="chicken", foodPrice=10.0, foodPriority=1)

    def test_menu(self):
        chicken = Menu.objects.get(foodName="chicken")
        self.assertEqual(chicken.foodName, "chicken")


class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(orderID=7, orderTime=datetime.now(), tableNum=1, payment=10.0)

    def test_order(self):
        order7 = Order.objects.get(orderID=7)
        self.assertEqual(order7.orderID, 7)
