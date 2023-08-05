from django.contrib import admin
from .models import Attempt


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['username', 'ipaddress', 'useragent', 'created']
