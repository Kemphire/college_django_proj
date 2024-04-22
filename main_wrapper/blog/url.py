from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.welcome, name="blog-home"),
    path('',views.welcome, name="blog-empty-home"),
    path('about/',views.about, name = "blog-about"),
]