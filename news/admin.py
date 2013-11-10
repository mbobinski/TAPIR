# -*- coding: utf-8 -*-
from django.contrib import admin

from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publicator', 'posted_date')


admin.site.register(News, NewsAdmin)