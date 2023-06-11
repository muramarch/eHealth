from django.db import models

from apps.accounts.models import User

class Hospital(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    contact_info = models.CharField(max_length=250)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        default=0.0
    )

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    rating = models.FloatField()
    

class Review(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()


