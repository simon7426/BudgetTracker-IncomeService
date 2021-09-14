from os import stat
from rest_framework import serializers
from budget_tracker_income_service.settings import SECRET_KEY
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Income, IncomeCategory
from .serializer import IncomeCategorySerializer, IncomeSerializer
from rest_framework.permissions import IsAuthenticated
import jwt
from rest_framework import status

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms='HS256')
        user_id = payload['user_id']
        return user_id
    except jwt.ExpiredSignatureError:
        return 'expired'
    except jwt.InvalidTokenError:
        return 'invalid'    
    except Exception as e:
        print(e)
        return 'fail'
        

class IncomeCategoryList(APIView):
    def get(self,request):
        if request.META.get('HTTP_AUTHORIZATION'):
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        else:
            token = ''
        user_id = decode_jwt_token(token)
        if user_id == 'expired':
            response_obj = {
            "status": "fail",
            "message": "Token Expired"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        elif user_id == 'invalid':
            response_obj = {
            "status": "fail",
            "message": "Token Invalid"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        elif user_id == 'fail':
            response_obj = {
            "status": "fail",
            "message": "Bad request"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        try:
            categories = IncomeCategory.objects.filter(income_category_owner=user_id,active_status=True)
            serializer = IncomeCategorySerializer(categories,many=True)

            response_obj = {
                "status": "success",
                "data": serializer.data
            }
            return Response(response_obj,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response_obj = {
                "status": "fail",
                "message": "Failed to retrive categories"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):
        if request.META.get('HTTP_AUTHORIZATION'):
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        else:
            token = ''
        user_id = decode_jwt_token(token)
        if user_id == 'expired':
            response_obj = {
            "status": "fail",
            "message": "Token Expired"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        elif user_id == 'invalid':
            response_obj = {
            "status": "fail",
            "message": "Token Invalid"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        elif user_id == 'fail':
            response_obj = {
            "status": "fail",
            "message": "Bad request"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)

        try: 
            data = request.data
            data['income_category_owner'] = user_id
            serializer = IncomeCategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                response_obj = {
                    "status": "success",
                    "message": "Successfully created category.",
                    "category_id": serializer.data.get('id')
                }
                return Response(response_obj,status=status.HTTP_201_CREATED)
            response_obj = {
                "status": "fail",
                "message": "Failed to create category."
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response_obj = {
                "status": "fail",
                "message": "Failed to create category"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
