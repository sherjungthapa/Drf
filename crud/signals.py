from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Employee

@receiver([post_delete,post_save],sender=Employee)
def invalid_cache_empolyee(sender,instance,*args, **kwargs):
    print("clear")
    cache.clear()