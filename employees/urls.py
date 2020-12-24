from django.urls import path

from employees.api import MessageApi

urlpatterns = [
    path('api', MessageApi.as_view())
]
