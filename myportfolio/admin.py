from django.contrib import admin
from django.apps import apps
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name']


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
