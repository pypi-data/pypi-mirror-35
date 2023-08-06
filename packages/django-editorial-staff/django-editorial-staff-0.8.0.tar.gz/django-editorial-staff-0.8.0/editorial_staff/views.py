# Imports from Django.  # NOQA
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView  # NOQA
from django.shortcuts import render_to_response  # NOQA
from django.urls import reverse_lazy


# Imports from editorial-staff.
from editorial_staff.data_providers import load_provider
from editorial_staff.forms import staffer_form
from editorial_staff.mixins import NavigationContextMixin
from editorial_staff.models import Staffer


DATA_PROVIDER, PROVIDER_MODULE, PROVIDER_OPTIONS = load_provider()


class Staffers(LoginRequiredMixin, NavigationContextMixin, View):
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


class StafferCreate(LoginRequiredMixin, NavigationContextMixin, CreateView):
    template_name = 'editorial_staff/staffer_create.html'
    model = Staffer

    form_class = staffer_form

    def get_context_data(self, **kwargs):
        """Add 'EDITORIAL_STAFF_EMAIL_DOMAIN' setting to context."""
        context = super(StafferCreate, self).get_context_data(**kwargs)

        email_domain = getattr(
            settings,
            'EDITORIAL_STAFF_EMAIL_DOMAIN',
            'example.com'
        )

        context.update({'mainEmailDomain': email_domain})

        context.update({'data_provider': DATA_PROVIDER})

        return context

    def get_success_url(self):
        submit_action = self.request.POST.get('submit', '_save')

        if submit_action == '_continue':
            return reverse_lazy('editorial_staff:staffer-edit', kwargs={
                'pk': self.object.id,
            })

        return reverse_lazy('editorial_staff:staffer-list')


class StafferUpdate(LoginRequiredMixin, NavigationContextMixin, UpdateView):
    template_name = 'editorial_staff/staffer_edit.html'
    model = Staffer

    form_class = staffer_form

    def get_context_data(self, **kwargs):
        context = super(StafferUpdate, self).get_context_data(**kwargs)

        context.update({'data_provider': DATA_PROVIDER})

        return context

    def get_success_url(self):
        submit_action = self.request.POST.get('submit', '_save')

        if submit_action == '_continue':
            return reverse_lazy(
                'editorial_staff:staffer-edit',
                kwargs=self.kwargs
            )

        return reverse_lazy('editorial_staff:staffer-list')


class StafferDetail(LoginRequiredMixin, NavigationContextMixin, RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'editorial_staff:staffer-edit'
