# Imports from Django.  # NOQA
from django.conf import settings
from django.utils.module_loading import import_string


# Imports from editorial-staff.
from editorial_staff.data_providers.slack import SlackProvider

__all__ = [
    'load_provider',
    'SlackProvider',
]


def load_provider():
    data_provider_path = getattr(
        settings,
        'EDITORIAL_STAFF_DATA_PROVIDER',
        None
    )
    data_provider_options = {}

    if data_provider_path is not None:
        try:
            DataProviderClass = import_string(data_provider_path)
            data_provider = DataProviderClass()
            data_provider_options = getattr(
                settings,
                'EDITORIAL_STAFF_DATA_PROVIDER_OPTIONS',
                {}
            )

            return data_provider, data_provider_path, data_provider_options
        except ImportError:
            pass

    return None, data_provider_path, data_provider_options
