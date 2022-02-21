import json

from rest_framework.test import APITestCase
from rest_framework import status

class CreateReadUpdateDeleteTest(APITestCase):

    def test_create_with_no_data(self):
        response = self.client.post("/api/contacts/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_missing_name(self):
        data = {
            "name": "",
            "phone_number": "543534534543",
            "email": "dolofanel@gmail.com"
        }
        response = self.client.post("/api/contacts/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_missing_email(self):
        data = {
            "name": "fddfgfd",
            "phone_number": "543534534543",
            "email": "sds@gmail.com"
        }
        response = self.client.post("/api/contacts/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_create(self):
        data = {
            "name": "testcase",
            "phone_number": "02752111382",
            "email": "dolofanel@gmail.com"
        }
        response = self.client.post("/api/contacts/", json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_contacts_list(self):
        response = self.client.get("/api/contacts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_individual_contact_get(self):
        response = self.client.get("/api/contacts/", kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client_details(self):
        data = {
            "name": "testcase",
            "phone_number": "02752111382",
            "email": "dolofanel@gmail.com"
        }
        response = self.client.put("/api/contacts/", json.dumps(data), content_type="application/json", kwargs={"pk":1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response)

    def test_delete_contact(self):
        response = self.client.delete("/api/contacts/", kwargs={"pk": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        