from django import views
from django.urls import path

from core_ui.views import header

urlpatterns = [
   path('header/',header, name='header'),
]