from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','city','phone_num','id']
    list_filter = ["user", "id"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    list_filter = ['id','name']