from django.db import models

from django_project.auth_.models import MyUser


class Product(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    link = models.ImageField(upload_to='products')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='products')
    genre = models.CharField(max_length=30)
    height = models.FloatField()
    width = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()


class Order(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name='orders')
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ordered')
    artist = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='orders')

    @property
    def price(self):
        result = 0

        for product in self.products.all():
            result += product.price

        return result
