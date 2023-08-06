# Imports from Django.  # NOQA
from django import forms
from django.forms.models import modelform_factory


# Imports from editorial-staff.
from editorial_staff.models import Staffer


staffer_form = modelform_factory(
    Staffer,
    fields=(
        'email',
        'first_name',
        'last_name',
        'active',
        'image_url',
        'full_name',
    ),
    widgets={
        'full_name': forms.HiddenInput()
    },
)
