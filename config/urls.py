from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from apps.chat.views import MessageListCreateView

from apps.hospitals.views import HospitalViewSet, DoctorViewSet, ReviewViewSet
from apps.accounts.views import UserViewSet, UserRegistrationAPIView


router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'message', MessageListCreateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/user-registration/', UserRegistrationAPIView.as_view(), name='user-registration'),
]
