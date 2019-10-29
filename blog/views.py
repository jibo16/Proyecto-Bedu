# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'home.html', context)


class PostListView(ListView):
	model = post
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']	

def about(request):
	return render(request, 'about.html', {'title': 'About'})