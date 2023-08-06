# Imports from Django.  # NOQA
from django.db.models.signals import post_save
from django.dispatch import receiver


# Imports from editorial-staff.
from editorial_staff.data_providers import load_provider
from editorial_staff.models import Staffer


DATA_PROVIDER, PROVIDER_MODULE, PROVIDER_OPTIONS = load_provider()


@receiver(post_save, sender=Staffer)
def notify_slack_on_staffer_create(sender, instance, created, **kwargs):
    """"""
    if created:
        if DATA_PROVIDER is not None:
            DATA_PROVIDER.post_new_staffer_message(PROVIDER_OPTIONS, instance)
