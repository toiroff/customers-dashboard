from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from accounts.models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class CustomerListView(ListCreateAPIView):
    queryset = Customer.objects.all()   
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomerUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    

class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()   
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    