from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import (
    Mcq_Serializer,
    Custom_user_Serializer,
    Submission_Serializer,
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
)
from .models import Mcq, Custom_user, Submission

import jwt



POSTIVE_MARKS_1 = 4
POSTIVE_MARKS_2 = 2

NEGATIVE_MARKS_1 = -2
NEGATIVE_MARKS_2 = -1



#TODO @permission_classes([IsAuthenticated])

from django.http import JsonResponse



@api_view(['GET'])
def all(request):
    allapies = [
        'api/token/refresh/',
        'api/token/',
        'register/',
    ]

    return Response({"All endpoint i am using" : allapies}, status=status.HTTP_200_OK)


class UserReg(APIView):
    def post(self, request,  *args, **kwargs):
        ser = UserRegistrationSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            cus_user = Custom_user(username=ser.validated_data['username'])
            cus_user.save()
            return Response({"messege": "Success"}, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    #
    # def post(self, request, *args, **kwargs):
    #     response = super().post(request, *args, **kwargs)
    #
    #         # secure_cookie = 'access_token=' + response.data['access'] + '; Secure; HttpOnly'
    #     response.set_cookie(key='access', value=response.data['access'], httponly=True, secure=True)
    #
    #     return response

class GetCurrentQuestion(APIView):
    def get(self, request, *args, **kwargs):
        pass

