from django.shortcuts import render
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookingForm()
    context = {'form':form}
    return render(request, 'book.html', context)