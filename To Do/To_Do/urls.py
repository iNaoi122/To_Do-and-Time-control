"""
Definition of urls for To_Do.
"""

from os import name
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
] 

