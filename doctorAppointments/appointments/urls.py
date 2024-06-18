from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('book', views.book, name="book"),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),

    
]