from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(blank=True) # Can add contacts without email
    phone_number = models.CharField(max_length=32, blank=True) # Can add contacts without number

    def __str__(self):
        return self.name # We get the name of contact