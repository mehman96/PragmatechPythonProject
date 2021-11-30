from django.contrib import admin

# Register your models here.
from .models import Contact,Tags

admin.site.register(Contact)
admin.site.register(Tags)