from budget_tracker_income_service.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Income, IncomeCategory
from .serializers import IncomeCategorySerializers, IncomeSerializers
from rest_framework.permissions import IsAuthenticated
import jwt

class IncomeCategoryList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        payload = jwt.decode(request.META.get('HTTP_AUTHORIZATION').split(' ')[-1],SECRET_KEY,algorithms='HS256')
        print(payload)

        content = {
            'status': 'Pass',
            'user_id': payload['user_id'] 
        }
        return Response(content)

