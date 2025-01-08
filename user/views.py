from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request):
        searializer = UserRegistrationSerializer(data=request.data)
        if searializer.is_valid():
            searializer.save()
            return Response({
                'status': "success",
                'message': 'User Created Successfully'
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': "error",
            'message': "User is already created"
        }, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    def post(self, request):
        pass

