from django.urls import path
from .views import hello

urlpatterns = [
    path("todoapps/", hello, name="top")
]