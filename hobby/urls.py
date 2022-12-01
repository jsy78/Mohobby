from django.urls import path
from . import views

app_name = "hobby"

urlpatterns = [
    path('create', views.create, name='create'),
    path('test', views.test, name='test'),
]
