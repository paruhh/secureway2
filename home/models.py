from django.db import models

# Create your models here.
from django.core.validators import (
    RegexValidator,
    MinLengthValidator
)
from django.core.exceptions import ValidationError


class Enquiry(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('completed', 'Completed'),
    ]


    INSURANCE_CHOICES = [
        ('Health', 'Health Insurance'),
        ('Life', 'Life Insurance'),
        ('Motor', 'Motor Insurance'),
        ('Travel', 'Travel Insurance'),
        ('Other', 'Other'),
    ]

    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Name should contain letters and spaces only.'
            )
        ]
    )

    phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[6-9][0-9]{9}$',
                message='Enter a valid 10-digit Indian mobile number.'
            )
        ]
    )

    email = models.EmailField(max_length=254)

    insurance_type = models.CharField(
        max_length=20,
        choices=INSURANCE_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    message = models.TextField(
        validators=[
            MinLengthValidator(
                10,
                message='Message must contain at least 10 characters.'
            )
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()

        if self.name and not self.name.strip():
            raise ValidationError({
                'name': 'Name cannot be empty.'
            })

        if self.message and not self.message.strip():
            raise ValidationError({
                'message': 'Message cannot be empty.'
            })

    
    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"