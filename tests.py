from django.test import TestCase
from django.contrib.auth.models import User
from .models import Contact, Group

class ContactManagerTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.contact = Contact.objects.create(name='Djoumessi Dylan', phone_number='653848259', email='djoumessi@gmail.com', address='odza Yaounde', user=self.user)
        self.group = Group.objects.create(name='Friends')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, 'Djoumessi Dylan')

    def test_group_creation(self):
        self.assertEqual(self.group.name, 'Friends')
