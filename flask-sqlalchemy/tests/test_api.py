import json
import pytest
import requests
from unittest import TestCase

# @pytest.mark.django_db
class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_empty_list(self) -> None: 
        companies_url = "http://192.168.0.20:8080/"
        response = requests.get(url = companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), [])