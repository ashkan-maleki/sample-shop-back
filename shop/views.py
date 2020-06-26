from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response

from shop.serializers import ProductSerializer, ProfileSerializer
from .models import Product, Profile


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def list(self, request, *args, **kwargs):
        current_user = self.request.user
        try:
            profile = current_user.profile
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=current_user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)