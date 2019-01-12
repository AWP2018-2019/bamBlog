# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

from app.models import UserProfile, Post, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = 'text', 'created_by', 'post'


admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)

