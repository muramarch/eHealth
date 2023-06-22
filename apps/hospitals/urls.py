from rest_framework import routers

from .views import DoctorViewSet, HospitalViewSet, ReviewViewSet, AppointmentViewSet  # Added "AppointmentViewSet"

router = routers.DefaultRouter()

router.register(r'hospitals', HospitalViewSet, basename='hospital')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'appointments', AppointmentViewSet, basename='appointment')  # Added "AppointmentViewSet"

urlpatterns = router.urls
