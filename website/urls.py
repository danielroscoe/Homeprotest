from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name="index"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('service.html',views.service,name="service"),
]