from django.shortcuts import render
from rest_framework import viewsets
from.serializer import EmployeSerializer
from.models import EmpolyeData

class EmployeModelViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeSerializer
    queryset = EmpolyeData.objects.all()