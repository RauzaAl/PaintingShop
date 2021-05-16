from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_project.exhibition.models import Exhibition, Picture
import os
import logging

logger = logging.getLogger('exhibition')


@receiver(post_delete, sender=Exhibition)
def auto_delete_link_on_delete(sender, instance, **kwargs):

    if instance.link:
        if os.path.isfile(instance.link.path):
            os.remove(instance.link.path)

            logger.info(f'Exhibition link deleted {instance.id}')


@receiver(post_delete, sender=Picture)
def auto_delete_link_on_delete(sender, instance, **kwargs):

    if instance.link:
        if os.path.isfile(instance.link.path):
            os.remove(instance.link.path)

            logger.info(f'Picture link deleted {instance.id}')