from django.db import models
from django.core.validators import RegexValidator

class Booking(models.Model):
    age = models.IntegerField()
    appointmentTime = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    dateOfBirth = models.DateField()
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    medic = models.CharField(max_length=200)
    personalNumericCode = models.CharField(max_length=13,
    validators=[RegexValidator(regex=r'^\d+$', message="Personal ID must be numeric.")])
    phoneNumber = models.CharField(max_length=12,
    validators=[RegexValidator(regex=r'^\+?4?\d{10,12}$',message='Please enter a valid phone mumber')])
    typeOfService = models.CharField(max_length=300)
    def __str__(self):
        return self.first_name
