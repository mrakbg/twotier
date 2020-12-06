from django.urls import path
from dojo import views

urlpatterns = [
    path('',views.home, name='dojo'),
    path('contact',views.contact, name='contact'),
]
