from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from shop.models import Product, Profile


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'id']
        read_only_fields = ['id']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['latitude', 'longitude', 'id']
        read_only_fields = ['id']

    def create(self, validated_data):
        current_user = validated_data.pop('user')

        try:
            profile = current_user.profile
            new_profile = Profile(**validated_data)
            profile.latitude = new_profile.latitude
            profile.longitude = new_profile.longitude
        except ObjectDoesNotExist:
            profile = Profile.objects.create(**validated_data)
            profile.user = current_user
            profile.save()

        return profile
