from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# TODO: what is the first parameter in the register() function?
router.register('property', views.PropertyListCreate)

# API endpoints
urlpatterns = [
    # rest_framework Router path
    path('', include(router.urls)),
    # GET: Returns a list of all users from the db
    path('user/', views.UserListCreate.as_view(), name='user'),

    # GET: Returns a list of all properties from the db
    # path('api/property/', views.PropertyListCreate),

    # GET: Returns a single property from the db
    path('property/<int:pk>/',
         views.PropertyDetailView.as_view(), name='PropertyDetail'),

    # POST: Create a new property booking record in the db
    path('property/<int:property_id>/book/', views.book, name='book'),

    # GET: Return a list of all bookings from the db
    path('booking/', views.BookingListCreate.as_view(), name='booking'),

    # GET: Return a list of all locations
    path('locations/', views.LocationListView.as_view(), name='locations'),

    # GET: Return a list of all experiences from the db
    path('experience/', views.ExperienceListCreate.as_view(), name='experience')
]
