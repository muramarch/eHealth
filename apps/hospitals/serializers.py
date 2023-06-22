from rest_framework import serializers

from apps.accounts.serializers import UserSerializer
from .models import Hospital, Doctor, Review, Appointment

class HospitalSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hospital
        fields = '__all__'

    def get_average_rating(self, hospital):
        reviews = Review.objects.filter(hospital=hospital)
        if reviews.exists():
            total_ratings = sum(review.rating for review in reviews)
            average_rating = total_ratings / reviews.count()
            return average_rating
        return None


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'
        

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
