# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import post

admin.site.register(post) # llama al modelo post desde models y lo presenta en el admin de django
