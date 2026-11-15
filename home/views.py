from django.shortcuts import render
from .forms import EnquiryForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Enquiry

def home(request):
    success = False

    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
            success = True
            form = EnquiryForm()
    else:
        form = EnquiryForm()

    return render(request, 'home/index.html', {
        'form': form,
        'success': success,
    })


def about(request):
    return render(request, 'home/about.html')

@staff_member_required
def dashboard(request):

    total_enquiries = Enquiry.objects.count()

    new_enquiries = Enquiry.objects.filter(
        status='new'
    ).count()

    contacted_enquiries = Enquiry.objects.filter(
        status='contacted'
    ).count()

    completed_enquiries = Enquiry.objects.filter(
        status='completed'
    ).count()

    context = {
        'total_enquiries': total_enquiries,
        'new_enquiries': new_enquiries,
        'contacted_enquiries': contacted_enquiries,
        'completed_enquiries': completed_enquiries,
    }

    return render(request, 'home/dashboard.html', context)