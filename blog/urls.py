# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'), # path para pagina principal
	path('about/', views.about, name='blog-about'), # path para pagina de informacion
	]