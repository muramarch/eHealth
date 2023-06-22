from .serializers import HospitalSerializer, DoctorSerializer, ReviewSerializer, AppointmentSerializer
from .models import Hospital, Doctor, Review, Appointment
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db.models import Q
from django.shortcuts import get_object_or_404


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    
    def get_queryset(self):
        queryset = Hospital.objects.all()
        name = self.request.query_params.get('name')
        location = self.request.query_params.get('location')
        specialization = self.request.query_params.get('specialization')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)

        return queryset

    @action(detail=True, methods=['POST'])
    def leave_review(self, request, pk=None):
        hospital = self.get_object()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, hospital=hospital)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()
        specialization = self.request.query_params.get('specialization')
        
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)
        
        return queryset
    
    @action(detail=True, methods=['GET', 'POST', 'PUT', 'DELETE'])
    def schedule(self, request, pk=None):
        doctor = self.get_object()
        
        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(doctor=doctor)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'PUT':
            appointment = get_object_or_404(Appointment, pk=pk, doctor=doctor)
            serializer = AppointmentSerializer(appointment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            appointment = get_object_or_404(Appointment, pk=pk, doctor=doctor)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
