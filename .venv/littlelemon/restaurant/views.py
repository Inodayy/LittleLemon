from rest_framework.decorators import api_view
from .models import Menu, Booking
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here. 
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

   # def get(self, request):
      #  return render(request, 'index.html', {})

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    #def get(self, request):
      #  return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    #def get(self, request):
        #  return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]
   
def index(request):
    return render(request, 'index.html', {})
    
    