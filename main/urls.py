from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# TODO: what is the first parameter in the register() function?
router.register('property', views.PropertyViewSet)
router.register('booking', views.BookingViewSet)
router.register('location', views.LocationViewSet)
router.register('user', views.UserViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('review',
                views.ReviewViewSet)
router.register('getAllBookingsForPropertyID',
                views.GetAllBookingsForPropertyID)

app_name = 'main'

# API endpoints
urlpatterns = [
    # rest_framework Router path
    path('', include(router.urls))
]
