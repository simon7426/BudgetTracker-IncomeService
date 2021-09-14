from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import IncomeCategory, Income

class IncomeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id','income_category_name','created_on','updated_on']
    
class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','user_id','income_category_id','account_id','description','amount','created_on','updated_on']
