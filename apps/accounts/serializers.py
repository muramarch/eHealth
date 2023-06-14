from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# doctor = User.objects.get(pk=1)  # Получение экземпляра класса Doctor из базы данных
# serializer = UserSerializer(doctor)  # Создание сериализатора
# serialized_data = serializer.data  # Получение сериализованных данных
# print(serialized_data)
