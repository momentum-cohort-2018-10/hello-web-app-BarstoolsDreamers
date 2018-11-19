from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import VolunteerForm
from collection.models import Volunteer
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    volunteers = Volunteer.objects.all()
    return render(request, 'index.html', {
        'volunteers': volunteers,
    })


def volunteer_detail(request, slug):
    volunteer = Volunteer.objects.get(slug=slug)
    return render(request, 'volunteers/volunteer_detail.html', {
        'volunteer': volunteer,
    })


@login_required
def edit_volunteer(request, slug):
    volunteer = Volunteer.objects.get(slug=slug)
    if volunteer.user != request.user:
        raise Http404
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


def create_volunteer(request):
    form_class = VolunteerForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = request.user
            volunteer.slug = slugify(volunteer.name)
            volunteer.save()
            return redirect('volunteer_detail', slug=volunteer.slug)
        else:
            form = form_class()
        return render(request, 'volunteers/create_volunteer.html', {
            'form': form,
        })
