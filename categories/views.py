from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework import permissions
# Create your views here.



# list of Category

class CategoryListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        # categories = Category.objects.filter(user_id=request.user.id)
        serialized_categories = CategorySerializer(categories, many=True)

        if categories.exists():
            return Response({
                'status': 'success',
                'message': 'Categories found',
                'data': serialized_categories.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'success',
                'message': 'No categories found',
                'data': []
            }, status=status.HTTP_200_OK)
        

# create a new Category

class CategoryCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # data = request.data
        # data['user_id'] = request.user.id

        searilized_data = CategorySerializer(data=request.data, context={'request': request})

        if searilized_data.is_valid():
            searilized_data.save()
            return Response({
                'status': 'success',
                'message': 'Category created successfully',
                'data': searilized_data.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Category not created',
            'data': searilized_data.errors
        }, status=status.HTTP_400_BAD_REQUEST)