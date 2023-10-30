from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.


class AppTesting(TestCase):

    def setUp(self):
        self.client = APIClient()

    def get_request(self, data=None):
        response = self.client.get("api/employee")
        self.assertEqual(response.staus_code, status.HTTP_200_OK)
