import uuid
import json

from django.test import TestCase
from rest_framework test import APIClient


class TestLibrary(TestCase):

    def test_checkout(self):
        self.client = APIClient()
        body = {
            "book_id": "1000",
            "member_id": "1"
        }
        response = self.client.post('/checkout', json.dumps(body))


    def test_checkout(self):
        self.client = APIClient()
        body = {
            "book_id": "1000",
            "member_id": "1"
        }
        response = self.client.post('/return', json.dumps(body))

    def test_fulfill(self):
        self.client = APIClient()
        body = {
            "book_id": "1000",
            "member_id": "1"
        }
        response = self.client.post('/return', json.dumps(body))