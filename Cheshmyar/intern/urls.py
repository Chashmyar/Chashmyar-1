from django.urls import path

from intern import views

urlpatterns = [
    path('', views.intern, name="intern"),
    path('submit/', views.submit, name='submit')
]