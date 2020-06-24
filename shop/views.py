from rest_framework import viewsets

from shop.serializers import ProductSerializer, CartSerializer
from .models import Product, Cart, CartItem


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
# from myapps.serializers import UserSerializer
# from rest_framework import viewsets
# from rest_framework.response import Response
#
# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         current_user = request.user
#         queryset = CartItem.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#
# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
