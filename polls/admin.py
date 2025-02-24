from django.contrib import admin
from .models import Poll, Option

class OptionInline(admin.TabularInline):
    model = Option

class PollAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Poll, PollAdmin)
