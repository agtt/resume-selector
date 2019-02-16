from django.contrib import admin
from .models import *


# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Experience, ExperienceAdmin)
