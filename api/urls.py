from django.urls import path
from .views import CustomerListView , ProductListView, OrderListView,CustomerUpdateDestroyView,ProductUpdateDestroyView,OrderUpdateDestroyView


urlpatterns = [
  path('customer/',CustomerListView.as_view(),name="customer-api"),
  path('product/',ProductListView.as_view(),name="product-api"),
  path('order/',OrderListView.as_view(),name="order-api"),

  path('customer/<int:pk>/',CustomerUpdateDestroyView.as_view(),name="customer-api"),
  path('product/<int:pk>/',ProductUpdateDestroyView.as_view(),name="product-api"),
  path('order/<int:pk>/',OrderUpdateDestroyView.as_view(),name="order-api"),
]