import json
from .models import Contact
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestCreate(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('contacts')

    def test_create_contact(self):
        data = {
            'name': 'test_name',
            'phone_number': '03453434',
            'email': 'test@gmail.com'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Should work because we want users to create contacts with just a name
    def test_create_with_name_only(self):
        data = {
            'name': 'test_name'
        }
        url = reverse('contacts')
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # These three should not work because name is mandatory
    def test_create_with_phone_number_only(self):
        data = {
            'phone_number': '07553434343'
        }
        url = reverse('contacts')
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_email_only(self):
        data = {
            'email': 'mail@gmail.com'
        }
        url = reverse('contacts')
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_mail_and_phone(self):
        data = {
            'phone_number': '0756454454',
            'email': 'mail@gmail.com'
        }
        url = reverse('contacts')
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_bad_email(self):
        data = {
            'name': 'name',
            'email': 'test',
            'phone_number': '064545454'
        }
        url = reverse('contacts')
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TestDelete(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # We need to create a contact, because django has a different database for testing
        cls.contact = Contact.objects.create(name='test_name', phone_number='test_number', email='test_email@gmail.com')

    def test_delete_contact(self):
        url = reverse('contact_detail', kwargs={'pk': self.contact.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUpdate(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            'name': 'dolofanel',
            'phone_number': '03453434',
            'email': 'soloist@gmail.com'
        }
        cls.contact = Contact.objects.create(name='test_name', phone_number='test_number', email='test_email@gmail.com')
        cls.url = reverse('contact_detail', kwargs={'pk': cls.contact.pk})

    def test_update_name(self):
        self.data['name'] = 'updated_name'
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_phone_number(self):
        self.data['phone_number'] = "07555555"
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_email(self):
        self.data['email'] = 'updated_email@gmail.com'
        response = self.client.put(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
