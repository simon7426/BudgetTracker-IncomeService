import json
from django.http import response
from django.utils.translation import activate
import os
from rest_framework import serializers, status
from django.test import TestCase
from rest_framework.test import APIClient
from budget_tracker_income_service.settings import SECRET_KEY

from core.models import Income,IncomeCategory
from core.serializer import IncomeSerializer
import jwt

class testIncome(TestCase):
    def setUp(self):
        self.client = APIClient()
        payload = {
            "user_id": 1
        }
        self.token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token)

    def test_006_get_all_incomes(self):
        test_category = IncomeCategory.objects.create(
            id = 1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        Income.objects.create(
            user_id = 1,
            income_category_id = test_category,
            account_id = 1,
            description = 'test_description',
            amount = 100,
        )
        Income.objects.create(
            user_id = 1,
            income_category_id = test_category,
            account_id = 2,
            description = 'test_description',
            amount = 105,
        )
        response = self.client.get('/income/')
        incomes = Income.objects.filter(user_id=1)
        serializers = IncomeSerializer(incomes,many=True)
        self.assertEqual(response.data.get('data'),serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_007_create_income(self):
        test_category = IncomeCategory.objects.create(
            id = 1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        data = {
            'income_category_id': 1,
            'account_id': 1,
            'description': 'another_test_description',
            'amount': 10
        }
        resp = self.client.post('/income/',json.dumps(data),content_type='application/json')
        self.assertEqual(resp.status_code,status.HTTP_201_CREATED)

    def test_008_get_income_id(self):
        test_category = IncomeCategory.objects.create(
            id = 1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        Income.objects.create(
            id = 1,
            user_id = 1,
            income_category_id = test_category,
            account_id = 1,
            description = 'test_description',
            amount = 100,
        )
        response = self.client.get('/income/1')
        income = Income.objects.get(pk=1)
        serializers = IncomeSerializer(income)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data.get('data'),serializers.data)

    def test_009_put_income_id(self):
        test_category = IncomeCategory.objects.create(
            id = 1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        Income.objects.create(
            id = 1,
            user_id = 1,
            income_category_id = test_category,
            account_id = 1,
            description = 'test_description',
            amount = 100,
        )
        data = {
            "income_category_id": 1,
            "account_id": 1,
            "description": "test_description_put",
            "amount": 100
        }
        response = self.client.put('/income/1',json.dumps(data),content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/income/1')
        self.assertEqual(response.data.get('data').get('description'),'test_description_put')
    
    def test_010_delete_income_id(self):
        test_category = IncomeCategory.objects.create(
            id = 1,
            income_category_name = 'test_category_1',
            income_category_owner = 1,
            active_status = True
        )
        Income.objects.create(
            id = 1,
            user_id = 1,
            income_category_id = test_category,
            account_id = 1,
            description = 'test_description',
            amount = 100,
        )
        response = self.client.delete('/income/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
