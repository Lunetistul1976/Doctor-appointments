from django.shortcuts import render

# Create your views here.
def book(request):
    return render(request, 'book.html')
def home(request):
    return render(request,'index.html')