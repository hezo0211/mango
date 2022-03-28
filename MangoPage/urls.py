from django.urls import path
from . import views

app_name = "MangoPage"
urlpatterns = [
    path('', views.index, name="index"),
]