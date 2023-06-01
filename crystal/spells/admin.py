from django.contrib import admin

from .models import Spell


class SpellAdmin(admin.ModelAdmin):
    list_display = ['name', 'vocation', 'x_max', 'y_max', 'x_min', 'y_min',
              'target_cap']


admin.site.register(Spell, SpellAdmin)
