from django.shortcuts import render,get_object_or_404,redirect
from .forms import BookingForm
from .models import Booking
from rest_framework.views import APIView
from .serializers import BookingSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

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
            redirect('/')
            form = BookingForm()
    context = {'form':form}
    return render(request, 'book.html', context)


class BookingDetailView(APIView):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        form = BookingForm(instance=booking)
        return render(request, 'booking_details.html', {'form': form, 'booking': booking})

    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)