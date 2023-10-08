from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Job)
class jobAdmin(admin.ModelAdmin):
    list_display = ['title','job_type','published_at','salary','experience']
    list_filter = ["salary", "experience"]

@admin.register(Category)
class CatgegoryAdmin(admin.ModelAdmin):
    pass