# Imports from Django.  # NOQA
from django.conf import settings


class NavigationContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(
            NavigationContextMixin,
            self
        ).get_context_data(**kwargs)

        context['navigation_options'] = {
            'logout_url': getattr(
                settings,
                'EDITORIAL_STAFF_LOGOUT_URL',
                None
            ),
        }

        return context
