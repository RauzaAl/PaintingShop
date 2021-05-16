from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_project.order.models import Product, Order
import logging

logger = logging.getLogger('order')


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:

        logger.info(f'Product with id {instance.id} created')
