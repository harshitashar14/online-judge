from django.urls import path
from ojuser import views
urlpatterns = [
    path('register', views.register),
]
