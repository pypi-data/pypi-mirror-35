# Imports from Django.  # NOQA
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.models import modelform_factory
from django.views.generic.base import RedirectView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView  # NOQA
from django.shortcuts import render_to_response  # NOQA
from django.urls import reverse_lazy


# Imports from editorial-staff.
from editorial_staff.models import Staffer  # NOQA


class Staffers(LoginRequiredMixin, View):
    def get(self, request):
        staff = Staffer.objects.all()

        latest_additions = Staffer.objects.order_by('-created')[:10]

        return render_to_response(
            'editorial_staff/staffer_list.html',
            {
                'latest_additions': latest_additions,
                'staff': staff
            }
        )


STAFFER_MODELFORM = modelform_factory(
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


class StafferCreate(LoginRequiredMixin, CreateView):
    template_name = 'editorial_staff/staffer_create.html'
    model = Staffer

    form_class = STAFFER_MODELFORM

    def get_context_data(self, *args, **kwargs):
        """Add 'STAFF_EMAIL_DOMAIN' setting to context."""
        context = super(StafferCreate, self).get_context_data(*args, **kwargs)

        email_domain = getattr(settings, 'STAFF_EMAIL_DOMAIN', 'example.com')

        context.update({'mainEmailDomain': email_domain})

        return context

    def get_success_url(self):
        submit_action = self.request.POST.get('submit', '_save')

        if submit_action == '_continue':
            return reverse_lazy('editorial_staff:staffer-edit', kwargs={
                'pk': self.object.id,
            })

        return reverse_lazy('editorial_staff:staffer-list')


class StafferUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'editorial_staff/staffer_edit.html'
    model = Staffer

    form_class = STAFFER_MODELFORM

    def get_success_url(self):
        submit_action = self.request.POST.get('submit', '_save')

        if submit_action == '_continue':
            return reverse_lazy(
                'editorial_staff:staffer-edit',
                kwargs=self.kwargs
            )

        return reverse_lazy('editorial_staff:staffer-list')


class StafferDetail(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'editorial_staff:staffer-edit'
