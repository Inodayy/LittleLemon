from django.test import TestCase, Client
from restaurant.models import Menu
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
        
    def setUp(self):
        self.menu1 = Menu.objects.create(id=5, title="IceCream", price=5, inventory=10)
        self.menu2 = Menu.objects.create(id=6, title="IceCream", price=10, inventory=35)
        
       
    def test_getall(self):
        user = User.objects.create_user(username='guestuser', password='pswd1234')
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/restaurant/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)