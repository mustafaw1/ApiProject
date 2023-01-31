from rest_framework.test import APITestCase
from rest_framework import status

class Api_test(APITestCase):
    def test_api(self):
        _data = {
            # "id" : "1",
            "name" : "Mustafa",
            "age" : "21",
            "city" : "Lahore"
        }
        _response = self.client.post("/api/v1/person/", data=_data, format="json")
        self.assertEqual(_response.status_code, status.HTTP_201_CREATED)



