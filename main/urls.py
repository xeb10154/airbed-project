from django.urls import path
from . import views

# API endpoints
urlpatterns = [
    # GET: Returns a list of all users from the db
    path('api/user/', views.UserListCreate.as_view(), name='user'),

    # GET: Returns a list of all properties from the db
    path('api/property/', views.PropertyListCreate.as_view(), name='property'),

    # GET: Returns a single property from the db
    path('api/property/<int:pk>/',
         views.PropertyDetailView.as_view(), name='PropertyDetail'),

    # POST: Create a new property booking record in the db
    path('api/property/<int:property_id>/book/', views.book, name='book'),

    # GET: Return a list of all bookings from the db
    path('api/booking/', views.BookingListCreate.as_view(), name='booking'),

    # GET: Return a list of all locations
    path('api/locations/', views.LocationListView.as_view(), name='locations'),

    # GET: Return a list of all experiences from the db
    path('api/experience/', views.ExperienceListCreate.as_view(), name='experience')
]
