# -*- coding: utf-8 -*-
from django.contrib import admin

from rank.models import Rank
from rank.models import RankLive

class RankAdmin(admin.ModelAdmin):
    list_display = ('name', 'participated', 'win', 'defeat', 'survive', 'destroyed', 'spoted', 'shootPercent', 'dmg', 'ocupated', 'defense', 'exp', 'severalExp', 'maxExp', 'date')

class RankLiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'participated', 'win', 'defeat', 'survive', 'destroyed', 'spoted', 'shootPercent', 'dmg', 'ocupated', 'defense', 'exp', 'severalExp', 'maxExp', 'date')


admin.site.register(Rank, RankAdmin)
admin.site.register(RankLive, RankLiveAdmin)