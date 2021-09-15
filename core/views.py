from os import stat
from re import L
from django.http.response import Http404
from rest_framework import serializers
from rest_framework import response
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
    
def check_invalid_token(user_id):
    if user_id == 'expired':
        response_obj = {
        "status": "fail",
        "message": "Token Expired"
        }
        return response_obj
    elif user_id == 'invalid':
        response_obj = {
        "status": "fail",
        "message": "Token Invalid"
        }
        return response_obj
    elif user_id == 'fail':
        response_obj = {
        "status": "fail",
        "message": "Bad request"
        }
        return response_obj

class IncomeCategoryList(APIView):
    def get(self,request):
        if request.META.get('HTTP_AUTHORIZATION'):
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
        else:
            token = ''
        user_id = decode_jwt_token(token)

        err = check_invalid_token(user_id)
        if err is not None:
            return Response(err,status=status.HTTP_400_BAD_REQUEST)

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

        err = check_invalid_token(user_id)
        if err is not None:
            return Response(err,status=status.HTTP_400_BAD_REQUEST)

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


class IncomeCategoryDetail(APIView):
    def get_object(self,request,pk,user_id):
        try:
            return IncomeCategory.objects.get(pk=pk,income_category_owner = user_id)
        except IncomeCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            if request.META.get('HTTP_AUTHORIZATION'):
                token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            else:
                token = ''
            user_id = decode_jwt_token(token)

            err = check_invalid_token(user_id)
            if err is not None:
                return Response(err,status=status.HTTP_400_BAD_REQUEST)

            income_category = self.get_object(request,pk,user_id)
            serializer = IncomeCategorySerializer(income_category)
            response_obj = {
                "status": "success",
                "message":"Category retrived successfully.",
                "data": serializer.data
            }
            return Response(response_obj,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            response_obj = {
                "status": "fail",
                "message": "Failed to retrive category."
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            if request.META.get('HTTP_AUTHORIZATION'):
                token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            else:
                token = ''
            user_id = decode_jwt_token(token)

            err = check_invalid_token(user_id)
            if err is not None:
                return Response(err,status=status.HTTP_400_BAD_REQUEST)
            
            data = request.data
            income_category = self.get_object(request,pk,user_id)
            data['income_category_owner'] = income_category.income_category_owner
            serializer = IncomeCategorySerializer(income_category,data=data)
            if serializer.is_valid():
                serializer.save()
                response_obj = {
                    "status": "success",
                    "message":"Successfully updated category",
                    "category_id": serializer.data.get('id')
                }
                return Response(response_obj, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response_obj = {
                "status": "fail",
                "message": "Failed to update category"
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            if request.META.get('HTTP_AUTHORIZATION'):
                token = request.META.get('HTTP_AUTHORIZATION').split(' ')[-1]
            else:
                token = ''
            user_id = decode_jwt_token(token)

            err = check_invalid_token(user_id)
            if err is not None:
                return Response(err,status=status.HTTP_400_BAD_REQUEST)
            
            income_category = self.get_object(request,pk,user_id)
            income_category.delete()
            response_obj = {
                "status": "success",
                "message": "Category deleted successfully."
            }
            return Response(response_obj, status = status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            response_obj = {
                "status": "fail",
                "message": "Failed to delete category."
            }
            return Response(response_obj,status=status.HTTP_400_BAD_REQUEST)
