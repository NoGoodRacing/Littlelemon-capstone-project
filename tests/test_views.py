from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="IceCream", price=80,
                                         inventory=100)
        self.item2 = Menu.objects.create(title="Choclate", price=40,
                                         inventory=10)
        self.client = Client()
        self.serializer = MenuSerializer([self.item1, self.item2],
                                         many=True)

    def test_getall(self):
        response = self.client.get(reverse("menu-items"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.serializer.data, response.data)
