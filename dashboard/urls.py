from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('lamar/',views.lamar),
    path('prank/',views.prank),
]