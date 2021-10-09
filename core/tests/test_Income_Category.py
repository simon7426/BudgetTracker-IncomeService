import json
from django.utils.translation import activate
import os
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient

from core.models import IncomeCategory
from core.serializer import IncomeCategorySerializer

class testIncomeCategory(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.token = os.environ.get('TEST_TOKEN')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        IncomeCategory.objects.create(
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        IncomeCategory.objects.create(
            income_category_name = 'test_category_2',
            income_category_owner = 1,
            active_status = False
        )
        IncomeCategory.objects.create(
            income_category_name = 'test_category_3',
            income_category_owner = 2,
            active_status = True
        )
    
    def test_001_get_all_income_categories(self):
        response = self.client.get('/income/category/')
        income_category = IncomeCategory.objects.filter(income_category_owner=1,active_status=True)
        serializers = IncomeCategorySerializer(income_category,many=True)
        # print(response.data.get('data'))
        # print(serializers.data)
        self.assertEqual(response.data.get('data'),serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_002_create_income_categories(self):
        data = {'income_category_name': 'test_category_4',
                'income_category_owner': 1,
        }
        resp = self.client.post('/income/category/',json.dumps(data),content_type='application/json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)