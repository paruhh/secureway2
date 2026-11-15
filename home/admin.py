from django.contrib import admin
from .models import Enquiry
# Register your models here.


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'email',
        'insurance_type',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'insurance_type',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
    )
    list_editable = ('status',)

    readonly_fields = ('created_at',)

    ordering = ('-created_at',)
