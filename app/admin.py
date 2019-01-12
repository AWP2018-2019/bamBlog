# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from app.models import UserProfile, Post, Comment

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)

