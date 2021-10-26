import json
from django.utils.translation import activate
import os
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from budget_tracker_income_service.settings import SECRET_KEY
import jwt

from core.models import IncomeCategory
from core.serializer import IncomeCategorySerializer

class testIncomeCategory(TestCase):
    def setUp(self):
        self.client = APIClient()
        payload = {
            "user_id": 1
        }
        self.token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
    
    def test_001_get_all_income_categories(self):
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
        response = self.client.get('/income/category/')
        income_category = IncomeCategory.objects.filter(income_category_owner=1,active_status=True)
        serializers = IncomeCategorySerializer(income_category,many=True)
        self.assertEqual(response.data.get('data'),serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_002_create_income_categories(self):
        data = {'income_category_name': 'test_category_1',
                'income_category_owner': 1,
        }
        resp = self.client.post('/income/category/',json.dumps(data),content_type='application/json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)
    
    def test_003_get_income_category_id(self):
        IncomeCategory.objects.create(
            id=1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        response = self.client.get('/income/category/1')
        income_category = IncomeCategory.objects.get(pk=1)
        serializers = IncomeCategorySerializer(income_category)
        self.assertEqual(response.data.get('data'),serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_004_put_income_category_id(self):
        IncomeCategory.objects.create(
            id=1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        data = {'income_category_name': 'test_category_put'}
        response = self.client.put('/income/category/1',json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/income/category/1')
        self.assertEqual(response.data.get('data').get('income_category_name'),'test_category_put')
        
    def test_005_delete_income_category_id(self):
        IncomeCategory.objects.create(
            id=1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        response = self.client.delete('/income/category/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)