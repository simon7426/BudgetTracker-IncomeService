from rest_framework import serializers
from budget_tracker_income_service.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Income, IncomeCategory
from .serializer import IncomeCategorySerializer, IncomeSerializer
from rest_framework.permissions import IsAuthenticated
import jwt
import logging
from rest_framework import status

logger = logging.getLogger(__name__)

class IncomeCategoryList(APIView):
    
    def get(self,request):
        payload = jwt.decode(request.META.get('HTTP_AUTHORIZATION').split(' ')[-1],SECRET_KEY,algorithms='HS256')
        user_id = payload['user_id']

        categories = IncomeCategory.objects.filter(income_category_owner=user_id,active_status=True)
        serializer = IncomeCategorySerializer(categories,many=True)

        return Response(serializer.data)
    
    def post(self,request):
        payload = jwt.decode(request.META.get('HTTP_AUTHORIZATION').split(' ')[-1],SECRET_KEY,algorithms='HS256')
        user_id = payload['user_id']
        data = request.data
        data['income_category_owner'] = user_id
        serializer = IncomeCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
