from django.contrib import admin
from .models import data1
# Register your models here.
class gameadmin(admin.ModelAdmin):
    list_display=('name')
admin.site.register(data1)