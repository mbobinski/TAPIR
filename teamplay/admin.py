# -*- coding: utf-8 -*-
from django.contrib import admin

from teamplay.models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'leader', 'persons', 'win', 'draw', 'defeat', 'date')


admin.site.register(Team, TeamAdmin)