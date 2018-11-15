from django.contrib import admin
# Register your models here.

from collection.models import Contact


class VolunteersAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Contact, VolunteersAdmin)
