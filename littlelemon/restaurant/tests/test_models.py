from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class MenuItemTest(TestCase):
    def test_get_item_str(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
    def test_getall(self):
            # Hacer petición GET a la vista que devuelve todos los menús
        response = self.client.get('/restaurant/menu/')  # Ajusta la URL según tu urls.py

            # Obtener todos los objetos Menu de la DB
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

            # Comparar los datos serializados con la respuesta de la vista
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='1234')
        self.client = APIClient()
        self.client.login(username='admin', password='1234')  # login del test
        # Crear instancias de prueba
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=150, inventory=50)


