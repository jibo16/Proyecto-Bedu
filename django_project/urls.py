# -*- coding: utf-8 -*-
from django.urls import path, include
from django.contrib import admin
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register' ),
    path('', include('blog.urls')), # pagina principal

]
