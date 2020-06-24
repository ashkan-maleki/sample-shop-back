from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from shop.models import Product, CartItem, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'id']
        read_only_fields = ['id']


# class CartSerializer(serializers.Serializer):
#     product = serializers.IntegerField()
#     count = serializers.IntegerField()

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'count', 'id']
        read_only_fields = ['id']

    def create(self, validated_data):
        current_user = validated_data.pop('user')

        try:
            cart = current_user.cart
        except ObjectDoesNotExist:
            cart = Cart()
            cart.user = current_user
            cart.payment = '0'
            cart.save()

        cart_item = CartItem(**validated_data)
        cart_item.cart = cart
        cart_item.save()

        return CartItem(**validated_data)

    def update(self, instance, validated_data):
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        return instance

#
#
# class CartSerializer(serializers.ModelSerializer):
#     cart_items = models.ManyToManyField('shop.Cart')
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     payment = models.CharField('پرداخت', max_length=20)
#
#
# class TransactionSerializer(serializers.ModelSerializer):
#     cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
#
#
# class ProfileSerializer(serializers.ModelSerializer):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     address = models.CharField('آدرس', max_length=250)
