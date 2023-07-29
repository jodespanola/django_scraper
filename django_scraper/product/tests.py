from . import models
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

class ProductTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Hanes Boys Girls Crewneck Sweatshirt ComfortBlend EcoSmart Kids Youth Low Pill",
            "price": "$13.18",
            "url": "https://www.ebay.com/itm/143597224639?hash=item216f0fc2bf%3Ag%3AJaYAAOSwOFtgK-Qv&_trkparms=%2526rpp_cid%253D5f04885bfd325e320a7a7b8b&var=442556672998",
            "image_url": "https://i.ebayimg.com/thumbs/images/g/JaYAAOSwOFtgK-Qv/s-l300.webp"
        }
        self.url = "/product/"

    def test_create_data(self):
        data = self.data
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.data.objects.latest('id').price, "$13.18")

    def test_create_data_without_name(self):
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_data_when_name_equals_blank(self):
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_data_without_price(self):
        data = self.data
        data.pop("price")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_data_when_price_equals_blank(self):
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_data_without_url(self):
        data = self.data
        data.pop("url")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_data_when_url_equals_blank(self):
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_data_without_image_url(self):
        data = self.data
        data.pop("image_url")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_data_when_image_url_equals_blank(self):
        data = self.data
        data["image_url"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_with_pagination(self):
        response = self.client.get(f'{self.url}?page=4')
        self.assertEqual(response.status_code, status.HTTP_200_OK)