from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = [
            'name',
            'phone',
            'email',
            'insurance_type',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True,
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 10-digit mobile number',
                'maxlength': '10',
                'inputmode': 'numeric',
                'required': True,
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'required': True,
            }),

            'insurance_type': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your insurance requirements',
                'rows': 4,
                'required': True,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if not name:
            raise forms.ValidationError('Please enter your name.')

        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError(
                'Enter a valid 10-digit mobile number.'
            )

        if phone[0] not in '6789':
            raise forms.ValidationError(
                'Enter a valid Indian mobile number.'
            )

        return phone

    def clean_message(self):
        message = self.cleaned_data['message'].strip()

        if len(message) < 10:
            raise forms.ValidationError(
                'Message must contain at least 10 characters.'
            )

        return message
