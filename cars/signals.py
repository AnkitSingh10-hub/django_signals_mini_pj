from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Car
import uuid
from buyers.models import Buyer

@receiver(pre_save, sender=Car)
def pre_save_modify_buyer_and_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-","").upper()[:10]
    
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()    
    
    
    