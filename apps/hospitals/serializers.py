from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from .models import Hospital, Doctor, Review

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        
# hospital = Hospital.objects.get(pk=1)  # Получение экземпляра класса Doctor из базы данных
# serializer = HospitalSerializer(hospital)  # Создание сериализатора
# serialized_data = serializer.data  # Получение сериализованных данных
# print(serialized_data)

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'
        
# doctor = Doctor.objects.get(pk=1)  # Получение экземпляра класса Doctor из базы данных
# serializer = DoctorSerializer(doctor)  # Создание сериализатора
# serialized_data = serializer.data  # Получение сериализованных данных
# print(serialized_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
# review = Review.objects.filter(pk=1).first()  # Получение экземпляра класса Doctor из базы данных
# serializer = ReviewSerializer(review)  # Создание сериализатора
# serialized_data = serializer.data  # Получение сериализованных данных
# print(serialized_data)
