from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.welcome, name="blog-home"),
    path('',views.welcome, name="blog-empty-home"),
    path('about/',views.about, name = "blog-about"),
    path('post/new',views.new_post_create, name = "post-creation"),
    path('post/<int:pk>/edit',views.post_edit, name = "post-edit"),
    path('post/<int:pk>',views.post_detail, name = "post-detail"),
    path('post/<int:pk>/delete',views.post_delete, name = "post-delete"),
]