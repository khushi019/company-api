from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class CompanyView(viewsets.ModelViewSet):
    
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    # company/{company.id}/employees
    # to get the employees of specific company
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emp=Employee.objects.filter(company=company)
            emp_serializer=EmployeeSerializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({'message':'This company does not exist'})



class EmployeeView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer    
