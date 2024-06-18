from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ('created_at',)
        labels = {
            'age': 'Age',
            'appointmentDateAndTime': 'Appointment Date and Time',
            'dateOfBirth': 'Date of Birth',
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'medic': 'Medic',
            'personalNumericCode': 'Personal Numeric Code',
            'phoneNumber': 'Phone Number',
            'typeOfService': 'Type of Service',
        }
