#from django.contrib import admin
from django.urls import path
from .views import StudentApi
urlpatterns = [
    path('', StudentApi.as_view()),
]
