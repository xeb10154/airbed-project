from django.urls import path
from . import views

# API endpoints
urlpatterns = [
    # GET: Returns a list of all users from the db
    path('api/user/', views.UserListCreate.as_view()),

    # GET: Returns a list of all properties from the db
    path('api/property/', views.PropertyListCreate.as_view()),

    # GET: Returns a single property from the db
    path('api/property/<int:pk>/',
         views.PropertyDetailView.as_view()),

    # POST: Create a new property booking record in the db
    path('api/property/<int:property_id>/book/', views.book),

    # GET: Return a list of all bookings from the db
    path('api/booking/', views.BookingListCreate.as_view()),

    # GET: Return a list of all experiences from the db
    path('api/experience/', views.ExperienceListCreate.as_view(),)
]
