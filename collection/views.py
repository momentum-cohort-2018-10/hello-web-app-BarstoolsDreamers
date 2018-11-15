from django.shortcuts import render
from collection.models import Contact


def index(request):
    volunteers = Contact.objects.all()
    return render(request, 'index.html', {
        'volunteers': volunteers,
    })
