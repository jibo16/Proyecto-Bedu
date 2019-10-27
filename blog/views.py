# -*- coding: utf-8 -*-
from django.shortcuts import render 
from django.http import HttpResponse
from .models import post

def home(request):
	context = {
		'posts': post.objects.all()
	}
	return render(request, 'home.html', context)

def about(request):
	return render(request, 'about.html', {'title': 'About'})