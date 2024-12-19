from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from orders.services import OrderService


@receiver(post_save, sender=Robot)
def handle_robot_creation(sender, instance, created, **kwargs):
    if created:
        OrderService.process_robot_availability(instance.serial)
