from django.shortcuts import render
from collection.models import Volunteer


def index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'index.html', {
        'volunteers': volunteers,
    })


def volunteer_detail(request, slug):
    volunteer = Volunteer.objects.get(slug=slug)
    return render(request, 'volunteer/volunteer_detail.html', {
        'volunteer': volunteer,
    })
