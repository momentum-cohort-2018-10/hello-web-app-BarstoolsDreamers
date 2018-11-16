from django.contrib import admin
# Register your models here.

from collection.models import Volunteer


class VolunteersAdmin(admin.ModelAdmin):
    model = Volunteer
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Volunteer, VolunteersAdmin)
