from accounts.models import Customer, Product, Order
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=False)
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = serializers.ChoiceField(choices=Product.CATEGORY)   
    tag = serializers.StringRelatedField(many=True)  # For ManyToMany relationships
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    product = ProductSerializer(read_only=True) 
    status = serializers.ChoiceField(choices=Order.STATUS)  
    date_created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
