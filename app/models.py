# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birthday = models.DateField(blank=True)

