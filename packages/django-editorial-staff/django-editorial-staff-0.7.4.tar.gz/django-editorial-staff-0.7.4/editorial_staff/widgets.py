# Imports from django.  # NOQA
from django.db.utils import ProgrammingError
from django import forms
from django.utils.safestring import mark_safe


# Imports from editorial-staff.
from editorial_staff.models import Vertical


class VerticalWidget(forms.widgets.Select):
    """A <select> widget that uses our staff API verticals as choices"""
    def __init__(self, *args, **kwargs):
        try:
            kwargs['choices'] = Vertical.objects.values_list('slug', 'name')
            return super(VerticalWidget, self).__init__(*args, **kwargs)
        except ProgrammingError:
            # For cases where the staff_vertical table isn't ready yet
            kwargs['choices'] = list()
            return super(VerticalWidget, self).__init__(*args, **kwargs)


class StafferSelectWidget(forms.Textarea):
    class Media:  # NOQA
        css = {
            'all': (
                'editorial_staff/staff-select-widget/css/selectize.css',
                'editorial_staff/staff-select-widget/css/staffer-select.css',
            )
        }
        js = (
            'editorial_staff/staff-select-widget/js/selectize.js',
            'editorial_staff/staff-select-widget/js/underscore.min.js',
            'editorial_staff/staff-select-widget/js/staffer-select.js',
        )

    def __init__(self, attrs=None, single_value=False):
        self.single_value = False
        if single_value:
            self.single_value = True
        super(StafferSelectWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        original_html = super(StafferSelectWidget, self).render(
            name,
            value,
            attrs,
        )

        if self.single_value:
            selection_class = 'single-value'
            placeholder_text = 'Select a staffer...'
        else:
            selection_class = 'multi-value'
            placeholder_text = 'Choose one or more staffers...'

        total_html = """
        <div class="staffer-select-outer """ + selection_class + """ ">
            <div class="original-html" style="display: none">
            """ + original_html + """
            </div>
            <select
                multiple
                class="staffer-select"
                placeholder='""" + placeholder_text + """'>
            </select>
        </div>
        """

        return mark_safe(total_html)
