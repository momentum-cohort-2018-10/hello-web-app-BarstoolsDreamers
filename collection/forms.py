from django.forms import ModelForm
from collection.models import Volunteer


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ('name', 'description',)
