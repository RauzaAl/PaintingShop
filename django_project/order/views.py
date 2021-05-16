import logging

from rest_framework import viewsets
from rest_framework.response import Response

from django_project.auth_.models import MyUser
from django_project.order.models import Product, Order
from django_project.order.serializers import ProductSerializer, OrderSerializer

logger = logging.getLogger('order')


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        author = MyUser.objects.get(id=self.request.data.get('author'))
        serializer.save(author=author)
        instance = serializer.save(author=author, client=self.request.user)

        logger.info(f'View created product, ID: {instance.id}')

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.request.user.role == 1:
            queryset = queryset.filter(client_id=self.request.user.id)
        else:
            queryset = queryset.filter(artist_id=self.request.user.id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)

    def perform_create(self, serializer):
        artist = MyUser.objects.get(id=self.request.data.get('artist'))
        instance = serializer.save(artist=artist, client=self.request.user)

