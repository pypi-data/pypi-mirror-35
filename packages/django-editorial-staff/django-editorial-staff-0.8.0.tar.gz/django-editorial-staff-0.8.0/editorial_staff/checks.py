# Imports from Django.  # NOQA
from django.conf import settings
from django.core.checks import Error
from django.core.checks import Info
from django.core.checks import register
from django.core.checks import Tags


SLACK_PROVIDER_PATH = 'editorial_staff.data_providers.SlackProvider'


MISSING_INSTALLED_APP_MSG = """django-editorial staff requires the app
'{}' to be available and installed.

Please ensure '{}' is in your INSTALLED_APPS list.
"""


MISSING_BOOTSTRAP_MSG = """django-editorial-staff noticed missing
Bootstrap-rendering configuration options.

Your staff pages will render, but some form elements may not be usable
until you add these settings.

Please consult the readme for django-editorial-staff, then add the
recommended configuration under the 'BOOTSTRAP3' name in your settings.
"""


MISSING_RENDERER_MSG = """A required Bootstrap renderer is missing:

>   BOOTSTRAP3['field_renderers']['{}']

Please specify the path to this utility -- it goes in the
'field_renderers' dictionary, which is inside the 'BOOTSTRAP3'
section of your settings file.

Until you do this, some form fields on django-editorial-staff pages may
not render correctly.
"""


MISSING_PROBABLEPEOPLE_MSG = """Missing dependency: probablepeople

You have django-editorial-staff set to use Slack for staffer data, but
the required 'probablepeople' library doesn't seem to be installed.

Please install probablepeople~=0.5.4 before proceeding.
"""


MISSING_SLACKER_MSG = """Missing dependency: slacker

You have django-editorial-staff set to use Slack for staffer data, but
the required 'slacker' library doesn't seem to be installed.

Please install slacker~=0.9.0 before proceeding.
"""


MISSING_SLACK_TOKEN_MSG = """Missing Slack API token

You have django-editorial-staff set to use Slack for staffer data, but
you don't have the necessary Slack API token in 'settings.SLACK_TOKEN'.

Your app will not be able to connect to Slack until you provide
this value.
"""


@register(Tags.compatibility)
def check_settings(app_configs, **kwargs):
    errors = []

    # Ensure needed helpers are in INSTALLED_APPS.
    required_helper_apps = ['bootstrap3', 'colorfield', 'rest_framework']

    for app_name in required_helper_apps:
        if app_name not in settings.INSTALLED_APPS:
            errors.append(Error(
                MISSING_INSTALLED_APP_MSG.format(app_name, app_name),
                id='editorial_staff.E001'
            ))

    # Ensure django-bootstrap is configured as expected, including the
    # DMN-style "Immaterial" field renderers.
    bootstrap_config = getattr(settings, 'BOOTSTRAP3', None)
    if bootstrap_config and 'field_renderers' in bootstrap_config:
        required_field_renderers = ['default', 'inline', 'immaterial']

        for renderer_key in required_field_renderers:
            if renderer_key not in bootstrap_config['field_renderers']:
                errors.append(Info(
                    MISSING_RENDERER_MSG.format(renderer_key),
                    id='editorial_staff.E002b'
                ))
    else:
        errors.append(Info(
            MISSING_BOOTSTRAP_MSG,
            id='editorial_staff.E002a'
        ))

    data_provider_path = getattr(
        settings,
        'EDITORIAL_STAFF_DATA_PROVIDER',
        None
    )
    if data_provider_path:
        if data_provider_path == SLACK_PROVIDER_PATH:
            # Slack provider requires the 'probablepeople' library.
            try:
                import probablepeople
            except ImportError:
                errors.append(Error(
                    MISSING_PROBABLEPEOPLE_MSG,
                    id='editorial_staff.E003a',
                ))

            # Slack provider requires the 'slacker' library.
            try:
                from slacker import Slacker
            except ImportError:
                errors.append(Error(
                    MISSING_SLACKER_MSG,
                    id='editorial_staff.E003b',
                ))

            # Slack provider needs the 'SLACK_TOKEN' setting to connect.
            slack_token = getattr(settings, 'SLACK_TOKEN', None)
            if not slack_token:
                errors.append(Error(
                    MISSING_SLACK_TOKEN_MSG,
                    id='editorial_staff.E004',
                ))

    return errors
