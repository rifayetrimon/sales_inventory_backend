from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.



# customer list 

class CustomerListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = Customer.objects.filter(user=request.user)
        serialized_customer = CustomerSerializer(customer, many=True)

        if customer.exists():
            return Response({
                'status': 'success',
                'message': 'Customer found',
                'data': serialized_customer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'success',
                'message': 'No customer found',
                'data': []
            }, status=status.HTTP_200_OK)
        

# create customer

class CustomerCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer_data = CustomerSerializer(data=request.data)

        if serializer_data.is_valid():
            serializer_data.save(user_id=request.user.id)
            return Response({
                'status': 'success',
                'message': 'Customer created successfully',
                'data': serializer_data.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Customer not created',
            'data': serializer_data.errors
        })
    

# update customer

class CustomerUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        customer_id = request.data.get('id')

        try:
            customer = Customer.objects.get(id=customer_id, user_id = request.user.id)
            serialized_customer = CustomerSerializer(customer, data=request.data)

            if serialized_customer.is_valid():
                serialized_customer.save()
                return Response({
                    'status': 'success',
                    'message': 'Customer updated successfully',
                    'data': serialized_customer.data
                }, status=status.HTTP_200_OK)
            return Response({
                'status': 'error',
                'message': 'Customer not updated',
                'data': serialized_customer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except Customer.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Customer not found',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)
        

# delete customer

class CustomerDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        customer_id = request.data.get('id')

        try:
            customer = Customer.objects.get(id=customer_id, user_id = request.user.id)
            customer.delete()
            return Response({
                'status': 'success',
                'message': 'Customer deleted successfully',
                'data': []
            }, status=status.HTTP_200_OK)
        
        except Customer.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Customer not found',
                'data': []
            }, status=status.HTTP_404_NOT_FOUND)