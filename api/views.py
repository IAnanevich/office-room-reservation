from django.shortcuts import render
from api.serializers import EmployeeSerializer, RoomSerializer, OfficeSerializer
from reservation.models import Employee, Room, Office
from rest_framework import viewsets


# Create your views here.
class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
