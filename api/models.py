from django.core.validators import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
import re
# Create your models here.

def validate_number(value):
    validation_regex = "(^[\d \-\+()]*$)"
    if not re.match(validation_regex, value):
        raise ValidationError(
            _('%(phone_number)s is not a valid phone number'),
            params={'phone_number': value},
        )


class Contact(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(blank=True, unique=True) # Can add contacts without email
    phone_number = models.CharField(max_length=32, validators=[validate_number], blank=True, unique=True ) # Can add contacts without number

    def __str__(self):
        return self.name
