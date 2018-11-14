from django.contrib import admin
# Register your models here.

from collection.models import Volunteers


class VolunteersAdmin(admin.ModelAdmin):
    model = Volunteers
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Volunteers, VolunteersAdmin)
