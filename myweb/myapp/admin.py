from django.contrib import admin

from django.contrib import admin

from .models import Person

# Register your models here.

class personAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    list_filter = ['name']
admin.site.register(Person, personAdmin)
