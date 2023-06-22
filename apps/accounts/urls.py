from rest_framework import routers

from .views import UserViewSet
from apps.hospitals.views import AppointmentViewSet  # Added "AppointmentViewSet"

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'appointments', AppointmentViewSet, basename='appointment')  # Added "AppointmentViewSet"

urlpatterns = router.urls
