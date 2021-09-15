from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import IncomeCategory, Income

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'
    
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
