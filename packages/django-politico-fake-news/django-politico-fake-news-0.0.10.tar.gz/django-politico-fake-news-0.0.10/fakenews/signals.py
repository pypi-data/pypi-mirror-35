import savepagenow
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

from .models import Claim
from .models import FactCheck


@receiver(pre_save, sender=Claim)
def update_archive_url(sender, instance, **kwargs):
    prev = sender.objects.filter(pk=instance.pk).first()

    # Existing object
    if prev is not None:
        if instance.canoncial_url == '':
            instance.archive_url = ''
        elif instance.canoncial_url != prev.canoncial_url:
            instance.archive_url = savepagenow.capture_or_cache(
                instance.canoncial_url
            )

    # New object
    else:
        instance.archive_url = savepagenow.capture_or_cache(
            instance.canoncial_url
        )


@receiver(pre_save, sender=FactCheck)
def update_publish_date(sender, instance, **kwargs):
        if(instance.status == 'pub' and instance.publish_date is None):
            instance.publish_date = datetime.now()

        if(not instance.status == 'pub'):
            instance.publish_date = None
