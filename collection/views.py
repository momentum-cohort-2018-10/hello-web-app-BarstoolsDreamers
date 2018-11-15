from django.shortcuts import render
from collection.models import Volunteers


def index(request):
    things = Volunteers.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })
