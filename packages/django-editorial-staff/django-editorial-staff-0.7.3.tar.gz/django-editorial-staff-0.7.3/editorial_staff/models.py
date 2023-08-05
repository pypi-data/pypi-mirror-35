# Imports from Django.  # NOQA
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Imports from editorial-staff.
from editorial_staff.utils import get_random_anonymous_animal


# Imports from other dependencies.
from colorfield.fields import ColorField


@python_2_unicode_compatible
class Vertical(models.Model):
    """Model for top-level organizational entities."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:  # NOQA
        ordering = ['name']

    def __str__(self):
        return self.name

    def as_object(self):
        return {
            'name': self.name,
            'slug': self.slug,
        }


class HubManager(models.Manager):
    def get_queryset(self):
        return super(
            HubManager,
            self
        ).get_queryset().select_related('vertical')


@python_2_unicode_compatible
class Hub(models.Model):
    """Model for lower-level organizational entities."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    vertical = models.ForeignKey(Vertical, on_delete=models.CASCADE)
    color = ColorField(default='#0185D3')

    objects = HubManager()

    class Meta:  # NOQA
        ordering = ['name']

    def __str__(self):
        return self.name

    def as_object(self):
        return {
            'name': self.name,
            'color': self.color,
            'slug': self.slug,
            'vertical': {
                'name': self.vertical.name,
                'slug': self.vertical.slug,
            }
        }


@python_2_unicode_compatible
class Staffer(models.Model):
    """Model for individual staffers."""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(
        blank=True,
        null=True,
        help_text='Usually auto-populated from Slack.'
    )
    active = models.BooleanField(default=True)

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    class Meta:  # NOQA
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            if not self.full_name:
                if self.first_name and self.last_name:
                    self.full_name = '{} {}'.format(
                        self.first_name,
                        self.last_name
                    )
                elif self.last_name and not self.first_name:
                    self.full_name = self.last_name

        if not self.last_name and not self.first_name:
            self.first_name = 'anonymous'
            self.last_name = get_random_anonymous_animal()

        super(Staffer, self).save(*args, **kwargs)

    def render_formatted_name(self):
        # TK: More error-proof formatting for people with the same
        # surname.
        return self.last_name

    def as_object(self):
        return {
            'firstName': self.first_name,
            'lastName': self.last_name,
            'fullName': self.full_name,
            'formattedName': self.render_formatted_name(),
            'email': self.email,
            'imageURL': self.image_url,
            'active': self.active,
        }
