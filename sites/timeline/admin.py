# -*- coding: UTF-8 -*-
from django.contrib import admin

from timeline.models import Timeline, TlEvent, Comment

admin.site.register(Timeline)
admin.site.register(TlEvent)
admin.site.register(Comment)
