from rest_framework import serializers

from django_project.auth_.serializers import UsersSerializer
from django_project.order.models import Product, Order
from django_project.utils.validators import validate_extension


class ProductSerializer(serializers.ModelSerializer):

    author = UsersSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'link', 'author', 'genre', 'height', 'width', 'created_at', 'price',)


class InnerProductSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'author', 'genre', 'height', 'width', 'created_at', 'price',)


class OrderSerializer(serializers.ModelSerializer):

    price = serializers.FloatField(read_only=True)
    client = UsersSerializer(read_only=True)
    artist = UsersSerializer(read_only=True)
    products = InnerProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'price', 'created_at', 'client', 'artist', 'products', )

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)

        for product in products:
            order.products.add(product.get('id'))
            p = Product.objects.get(id=product.get('id'))
            p.orders.add(order.id)
            p.save()

        order.save()

        return order
