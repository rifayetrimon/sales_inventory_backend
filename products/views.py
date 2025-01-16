from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework import permissions

# Create your views here.


# view all Product

class ProductListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.filter(user=request.user)
        serialized_products = ProductSerializer(products, many=True)

        if products.exists():
            return Response({
                'status': 'success',
                'message': 'Products found',
                'data': serialized_products.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'success',
                'message': 'No products found',
                'data': []
            }, status=status.HTTP_200_OK)
        

# create Product

class ProductCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serialized_product = ProductSerializer(data=request.data)

        if serialized_product.is_valid():
            serialized_product.save(user_id = request.user.id)
            return Response({
                'status': 'success',
                'message': 'Product created successfully',
                'data': serialized_product.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 'error',
                'message': 'Product not created',
                'data': serialized_product.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        


# update Product

class ProductUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        product_id = request.data.get('id')

        try:
            product = Product.objects.get(id=product_id, user_id = request.user.id)
            serialized_product = ProductSerializer(product, data=request.data)

            if serialized_product.is_valid():
                serialized_product.save()
                return Response({
                    'status': 'success',
                    'message': 'Product updated successfully',
                    'data': serialized_product.data
                }, status=status.HTTP_200_OK)
            return Response({
                'status': 'error',
                'message': 'Product not updated',
                'data': serialized_product.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Product not found',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)
    

# delete Product

class ProductDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        product_id = request.data.get('id')

        try:
            product = Product.objects.get(id=product_id, user_id = request.user.id)
            product.delete()
            return Response({
                'status': 'success',
                'message': 'Product deleted successfully',
                'data': []
            }, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Product not found',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)



# see a product details 

class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk, user_id = request.user.id)
            serialized_product = ProductSerializer(product)
            return Response({
                'status': 'success',
                'message': 'Product found',
                'data': serialized_product.data
            }, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Product not found',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)