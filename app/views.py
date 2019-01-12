# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView

from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):

    template_name = "index.html"