from rest_framework import serializers
from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user_id', 'name', 'phone', 'email', 'created_at', 'updated_at']

