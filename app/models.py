# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    text = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)
        
class Comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments")
    created_by = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} created by {} at {}".format(self.text, self.created_by.username, self.created_at)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birthday = models.DateField(blank=True)

