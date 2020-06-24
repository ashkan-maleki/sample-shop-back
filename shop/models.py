from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField('نام کالا', max_length=150)
    price = models.CharField('قیمت', max_length=20)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    payment = models.CharField('پرداخت', max_length=20)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
    count = models.IntegerField('تعداد')

    def __str__(self):
        return f'{self.product.name} ({self.count})'


class Transaction(models.Model):
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    address = models.CharField('آدرس', max_length=250)
