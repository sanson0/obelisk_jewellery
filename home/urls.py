from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('deliver', views.deliver, name='deliver'),
    path('payment', views.payment, name='payment'),
    path('ts_and_cs', views.ts_and_cs, name='ts_and_cs'),
]
