from django.shortcuts import render
from .forms import BookingForm
from .models import Booking

# Create your views here.

def home(request):
    bookings_list = Booking.objects.all()
    bookings_data = {'bookings':bookings_list}    
    return render(request,'index.html',bookings_data)

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookingForm()
    context = {'form':form}
    return render(request, 'book.html', context)