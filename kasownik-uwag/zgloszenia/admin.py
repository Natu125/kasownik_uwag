from django.contrib import admin

from .models import Dzial, Zgloszenie


admin.site.register(Dzial)


@admin.register(Zgloszenie)
class ZgloszenieAdmin(admin.ModelAdmin):
    filter_horizontal = ("dzialy",)