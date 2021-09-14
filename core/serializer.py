from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import IncomeCategory, Income

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id','income_category_name','income_category_owner','active_status','created_on','updated_on']
    
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','user_id','income_category_id','account_id','description','amount','created_on','updated_on']
