from django.shortcuts import render, redirect
from collection.forms import VolunteerForm
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


def edit_volunteer(request, slug):
    volunteer = Volunteer.objects.get(slug=slug)
    form_class = VolunteerForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('volunteer_detail', slug=volunteer.slug)
    else:
        form = form_class(instance=volunteer)
    return render(request, 'volunteers/edit_volunteer.html', {
        'volunteer': volunteer,
        'form': form,
    })
