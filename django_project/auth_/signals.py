import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_project.auth_.models import MyUser, Profile

logger = logging.getLogger('auth_')


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f'Profile for user with id {instance.id} created')


@receiver(post_delete, sender=MyUser)
def user_deleted(sender, instance, **kwargs):
    Profile.objects.delete(user=instance)

    logger.info(f'Profile deleted, ID: {instance.id}')