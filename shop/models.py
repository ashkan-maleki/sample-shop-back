from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField('نام کالا', max_length=150)
    price = models.CharField('قیمت', max_length=20)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.CharField('عرض جغرافیایی', max_length=20, blank=True)
    longitude = models.CharField('طول جغرافیایی', max_length=20, blank=True)

    def __str__(self):
        return self.user.username
