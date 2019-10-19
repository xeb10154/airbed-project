from django.urls import path
from . import views

urlpatterns = [
    path('api/user/', views.UserListCreate.as_view()),
    path('api/property/<int:property_id>/book/', views.book),
    path('api/booking/', views.BookingListCreate.as_view()),
]
