from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="pages"),
    path('about-us', views.about_us, name="about-us"),
    path('contact', views.contact, name="contact")
]