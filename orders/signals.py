from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from .models import Order


@receiver(m2m_changed, sender=Order.cars.through)
def m2m_changed_cars_order(sender, instance, action, **kwargs):
    print('running')
    total = 0
    total_price = 0
    for car in instance.cars.all():
        total = total +1
        total_price = car.price
        
    instance.total = total
    instance.total_price = total_price
    instance.save()    


