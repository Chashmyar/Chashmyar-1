from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<str:post_title>', views.blog_single, name="blog-single")
]
