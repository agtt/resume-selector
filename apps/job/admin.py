from django.contrib import admin
from .models import *


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    pass


class IndustryAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Section, SectionAdmin)
