from django.urls import path
from . import views

urlpatterns = [
    path('api/main/', views.UserListCreate.as_view()),
]
