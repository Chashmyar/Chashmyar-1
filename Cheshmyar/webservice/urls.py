from django.urls import path

from webservice import views

urlpatterns = [
    path('', views.webservice, name="webservice")
]