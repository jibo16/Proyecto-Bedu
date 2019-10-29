# -*- coding: utf-8 -*-
from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='blog-home'), # path para pagina principal
	path('about/', views.about, name='blog-about'), # path para pagina de informacion
	]